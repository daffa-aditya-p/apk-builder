# GitHub Actions Workflow

This directory contains the GitHub Actions workflow for building APK in the cloud.

## 📄 Files

- `build-apk.yml` - Main workflow untuk build Android APK

## 🚀 How It Works

### Trigger

Workflow ini dapat di-trigger dengan 2 cara:

1. **Manual (workflow_dispatch)**
   ```
   Go to: https://github.com/username/apk-builds/actions
   Select: "Build Android APK"
   Click: "Run workflow"
   ```

2. **Automatic (push)**
   - Setiap ada push ke `build-config.json`
   - Setiap ada push ke folder `www/`

### Workflow Steps

1. **Checkout code** - Download repository
2. **Setup Node.js** - Install Node.js 18
3. **Setup Java** - Install Java 17
4. **Install Cordova** - Install Cordova globally
5. **Read Configuration** - Parse `build-config.json`
6. **Create Cordova Project** - Generate Android project structure
7. **Copy Web Files** - Copy project files ke `www/`
8. **Configure Cordova** - Setup permissions, version, dll
9. **Copy Icon** - Copy icon jika ada
10. **Build APK** - Compile menjadi APK
11. **Rename APK** - Beri nama sesuai app name & version
12. **Upload APK** - Upload sebagai artifact
13. **Create Release** - (Optional) Create GitHub release

### Build Configuration

Workflow membaca dari `build-config.json`:

```json
{
  "app_name": "My App",
  "app_id": "com.example.myapp",
  "version": "1.0.0",
  "version_code": 1,
  "permissions": [
    "android.permission.INTERNET",
    "android.permission.CAMERA"
  ],
  "display_options": {
    "orientation": "portrait",
    "fullscreen": false,
    "statusbar": true
  }
}
```

## 🔧 Customization

### Modify Build Process

Edit `build-apk.yml` untuk customize:

**Change Android SDK version:**
```yaml
- name: Create Cordova Project
  run: |
    cordova create apk-project ${{ steps.config.outputs.app_id }} "${{ steps.config.outputs.app_name }}"
    cd apk-project
    cordova platform add android@12.0.0  # Specify version
```

**Add plugins:**
```yaml
- name: Add Cordova Plugins
  run: |
    cd apk-project
    cordova plugin add cordova-plugin-camera
    cordova plugin add cordova-plugin-geolocation
```

**Change build type:**
```yaml
- name: Build APK
  run: |
    cd apk-project
    cordova build android --debug  # Debug build instead of release
```

### Environment Variables

Add secrets di GitHub:

1. Go to: `Settings` → `Secrets and variables` → `Actions`
2. Add secrets:
   - `KEYSTORE_FILE` - Base64 encoded keystore
   - `KEYSTORE_PASSWORD` - Keystore password
   - `KEY_ALIAS` - Key alias
   - `KEY_PASSWORD` - Key password

Use in workflow:
```yaml
- name: Sign APK
  env:
    KEYSTORE_PASSWORD: ${{ secrets.KEYSTORE_PASSWORD }}
  run: |
    # Sign APK command
```

## 📊 Monitoring

### View Build Logs

1. Go to: `https://github.com/username/apk-builds/actions`
2. Click on workflow run
3. Click on job
4. View logs for each step

### Download Artifacts

1. Wait for build to complete
2. Go to workflow run page
3. Scroll to "Artifacts"
4. Click to download

Artifacts expire after 30 days by default.

### Check Status

Via GitHub API:
```bash
curl -H "Authorization: token YOUR_TOKEN" \
  https://api.github.com/repos/username/apk-builds/actions/runs
```

## 🐛 Troubleshooting

### Build Failed

1. Check logs untuk error message
2. Common issues:
   - Missing files di `www/`
   - Invalid `build-config.json`
   - Cordova plugin errors
   - Android SDK issues

### Workflow Not Triggering

1. Check workflow file syntax
2. Verify trigger conditions
3. Check repository permissions
4. Verify GitHub token scope

### Artifact Not Found

1. Check if build completed successfully
2. Verify artifact upload step passed
3. Check artifact retention period

## 📝 Notes

- Build time: ~5-10 minutes
- Free tier: 2000 minutes/month
- Concurrent builds: Limited by GitHub plan
- Artifacts retention: 30 days (configurable)

## 🔗 References

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Cordova Documentation](https://cordova.apache.org/docs/)
- [Android Build Documentation](https://cordova.apache.org/docs/en/latest/guide/platforms/android/)

---

**For more info, see main [README.md](../../README.md)**
