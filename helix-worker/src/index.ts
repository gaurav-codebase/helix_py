interface HelixParameters {
  radius: number;
  pitch: number;
  num_turns: number;
  points_per_turn: number;
  num_base_pairs: number;
}

interface Point3D {
  x: number[];
  y: number[];
  z: number[];
}

interface BasePair {
  x: [number, number];
  y: [number, number];
  z: [number, number];
}

interface HelixResponse {
  strand1: Point3D;
  strand2: Point3D;
  base_pairs: BasePair[];
}

// Validation function
function validateParameters(params: HelixParameters): string | null {
  if (params.radius < 0.5 || params.radius > 3.0) return "Radius must be between 0.5 and 3.0";
  if (params.pitch < 1.0 || params.pitch > 5.0) return "Pitch must be between 1.0 and 5.0";
  if (params.num_turns < 1 || params.num_turns > 20) return "Number of turns must be between 1 and 20";
  if (params.points_per_turn < 50 || params.points_per_turn > 200) return "Points per turn must be between 50 and 200";
  if (params.num_base_pairs < 5 || params.num_base_pairs > 50) return "Number of base pairs must be between 5 and 50";
  return null;
}

// Helper function to generate linear space array
function linspace(start: number, stop: number, num: number): number[] {
  const step = (stop - start) / (num - 1);
  return Array.from({ length: num }, (_, i) => start + step * i);
}

// Helper function to generate cos array
function cos(arr: number[]): number[] {
  return arr.map(x => Math.cos(x));
}

// Helper function to generate sin array
function sin(arr: number[]): number[] {
  return arr.map(x => Math.sin(x));
}

export default {
  async fetch(request: Request): Promise<Response> {
    // Handle CORS
    const corsHeaders = {
      "Access-Control-Allow-Origin": "*", // Allow all origins in development
      "Access-Control-Allow-Methods": "POST, OPTIONS, GET",
      "Access-Control-Allow-Headers": "Content-Type",
    };

    if (request.method === "OPTIONS") {
      return new Response(null, {
        headers: corsHeaders,
      });
    }

    // Handle GET requests with a helpful message
    if (request.method === "GET") {
      const helpMessage = {
        message: "Welcome to the Double Helix Generator API",
        usage: {
          method: "POST",
          endpoint: "/",
          body: {
            radius: "number (0.5-3.0)",
            pitch: "number (1.0-5.0)",
            num_turns: "number (1-20)",
            points_per_turn: "number (50-200)",
            num_base_pairs: "number (5-50)"
          }
        }
      };

      return new Response(JSON.stringify(helpMessage), {
        status: 200,
        headers: {
          ...corsHeaders,
          "Content-Type": "application/json"
        }
      });
    }

    // Only accept POST requests for actual helix generation
    if (request.method !== "POST") {
      return new Response(JSON.stringify({ error: "Only POST method is allowed" }), { 
        status: 405,
        headers: {
          ...corsHeaders,
          "Content-Type": "application/json"
        }
      });
    }

    try {
      const params: HelixParameters = await request.json();
      
      // Validate parameters
      const validationError = validateParameters(params);
      if (validationError) {
        return new Response(JSON.stringify({ error: validationError }), {
          status: 400,
          headers: {
            ...corsHeaders,
            "Content-Type": "application/json",
          },
        });
      }

      // Generate helix points
      const numPoints = params.points_per_turn * params.num_turns;
      const t = linspace(0, 2 * Math.PI * params.num_turns, numPoints);
      
      // First strand
      const x1 = cos(t).map(x => x * params.radius);
      const y1 = sin(t).map(x => x * params.radius);
      const z1 = t.map(x => (params.pitch * x) / (2 * Math.PI));
      
      // Second strand
      const x2 = cos(t.map(x => x + Math.PI)).map(x => x * params.radius);
      const y2 = sin(t.map(x => x + Math.PI)).map(x => x * params.radius);
      const z2 = z1;

      // Generate base pairs
      const indices = linspace(0, numPoints - 1, params.num_base_pairs)
        .map(x => Math.round(x));
      
      const base_pairs = indices.map(idx => ({
        x: [x1[idx], x2[idx]],
        y: [y1[idx], y2[idx]],
        z: [z1[idx], z2[idx]],
      }));

      const response = {
        strand1: {
          x: x1,
          y: y1,
          z: z1,
        },
        strand2: {
          x: x2,
          y: y2,
          z: z2,
        },
        base_pairs,
      };

      return new Response(JSON.stringify(response), {
        headers: {
          ...corsHeaders,
          "Content-Type": "application/json",
        },
      });
    } catch (error) {
      return new Response(JSON.stringify({ 
        error: "Invalid request format. Expected JSON with radius, pitch, num_turns, points_per_turn, and num_base_pairs" 
      }), {
        status: 400,
        headers: {
          ...corsHeaders,
          "Content-Type": "application/json",
        },
      });
    }
  },
}; 