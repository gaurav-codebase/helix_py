# Project Setup

This project uses Git submodules. To clone the repository with all submodules, use:

```bash
git clone --recursive git@github.com:yourusername/helix-py.git
```

If you already cloned the repository without `--recursive`, initialize the submodules with:

```bash
git submodule update --init --recursive
```

### Updating Submodules

To update the frontend submodule to the latest version:

```bash
git submodule update --remote frontend
```

---




# Git Submodule Setup for helix_py

This guide explains how to set up and manage the frontend as a Git submodule in the helix_py project.

## Initial Setup

### 1. Prepare Existing Frontend
```bash
# From the root directory of helix_py
git rm --cached frontend
rm -rf frontend/.git
```

### 2. Create Frontend Repository
1. Create a new repository on GitHub/GitLab for the frontend code (e.g., 'helix-frontend')
2. Set up the frontend repository:
```bash
# Navigate to frontend directory
cd frontend

# Initialize new git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial frontend commit"

# Add remote repository (replace with your repository URL)
git remote add origin git@github.com:yourusername/helix-frontend.git

# Push to remote repository
git push -u origin main
```

### 3. Add Frontend as Submodule
```bash
# Navigate back to root directory
cd ..

# Remove existing frontend directory
rm -rf frontend

# Add the submodule (replace with your repository URL)
git submodule add git@github.com:yourusername/helix-frontend.git frontend

# Commit the changes
git add .gitmodules frontend
git commit -m "Add frontend as submodule"
```

## Cloning the Project

### Fresh Clone
To clone the repository with all submodules:
```bash
git clone --recursive git@github.com:yourusername/helix-py.git
```

### Existing Clone
If you already cloned the repository without `--recursive`:
```bash
git submodule update --init --recursive
```

## Working with the Submodule

### Making Changes
```bash
# Navigate to frontend directory
cd frontend

# Make your changes
# Then commit and push
git add .
git commit -m "Update frontend"
git push

# Navigate back to main project
cd ..

# Update submodule reference
git add frontend
git commit -m "Update frontend submodule reference"
git push
```

### Pulling Updates
When there are updates to the frontend submodule:
```bash
# Pull updates in main repository
git pull

# Update submodules
git submodule update --remote frontend
```

## Useful Commands

### Check Submodule Status
```bash
git submodule status
```

### Update All Submodules
```bash
git submodule update --remote
```

### Execute Command in Submodule
```bash
git submodule foreach 'git checkout main'
```

### Remove Submodule (if needed)
```bash
git submodule deinit frontend
git rm frontend
git commit -m "Remove frontend submodule"
# Then delete the relevant section from .gitmodules
```

## Best Practices

1. Always commit and push changes in the submodule first
2. Then update the reference in the main repository
3. Use SSH URLs for submodules when possible (easier for CI/CD)
4. Keep the submodule on a specific branch or tag
5. Document any submodule-specific configuration in the project README

## Troubleshooting

### Common Issues

1. **Submodule appears empty:**
   ```bash
   git submodule update --init --recursive
   ```

2. **Submodule is in a detached HEAD state:**
   ```bash
   cd frontend
   git checkout main
   ```

3. **Submodule updates not reflecting:**
   ```bash
   git submodule update --remote --merge
   ```

### Prevention Tips

1. Always check if you're in the correct directory before making changes
2. Regularly update both the main repository and submodules
3. Use `git status` to verify the state of your repositories
4. Keep your local branches up to date with remote

## Project Structure After Setup

Your project structure should look like this:

helix_py/
├── .git/
├── .gitmodules # Contains submodule configurations
├── frontend/ # Submodule directory
│ ├── .git # Submodule's git directory
│ ├── src/
│ ├── package.json
│ └── ...
├── helix_project/
├── helix_app/
└── ...


## Additional Resources

- [Git Submodules Documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
- [Git Submodules Cheat Sheet](https://gist.github.com/gitaarik/8735255)

---

For any questions or issues, please refer to the project maintainers or create an issue in the repository.
