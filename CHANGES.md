# Changes from Upstream RustDesk

This document lists all modifications made to the upstream RustDesk (v1.4.5) codebase
for the Metroid Remote Support branded fork.

## Rebranding Changes

### Identity
- Changed `APP_NAME` from `"RustDesk"` to `"Metroid-RS"` (`libs/hbb_common/src/config.rs`)
- Changed `ORG` from `"com.carriez"` to `"com.metroid"` (`libs/hbb_common/src/config.rs`)
- Updated `Cargo.toml`: binary name `metroid-rs`, authors, description, winres metadata, bundle identifier
- Added `[[bin]]` entry for `metroid-rs` in root `Cargo.toml`
- Updated CLI entry point in `src/main.rs`
- Changed TOTP issuer from `"RustDesk"` to `"Metroid Remote Support"` (`src/auth_2fa.rs`)
- Changed portable env key from `RUSTDESK_APPNAME` to `METROIDRS_APPNAME` (`src/common.rs`, `flutter/lib/consts.dart`)
- Updated `libs/portable/Cargo.toml` with Metroid branding

### Platform Configurations
- **Android**: Updated `AndroidManifest.xml` (label, URL scheme), `strings.xml`, `build.gradle` (applicationId)
- **iOS**: Updated `Info.plist` (display name, bundle name, URL scheme, bundle URL name)
- **macOS**: Updated `AppInfo.xcconfig` (product name, bundle ID, copyright), `Info.plist` (URL scheme)
- **Windows**: Updated `Runner.rc` (company, description, internal name, copyright, product name)
- **Linux**: Updated `CMakeLists.txt` (binary name, application ID)
- **Windows Flutter**: Updated `CMakeLists.txt` (binary name)

### UI Text
- Updated About dialog copyright text and background color (`desktop_setting_page.dart`)
- Updated mobile settings page website display text (`settings_page.dart`)

### Colors (Metroid Brand Palette)
- Primary Dark Blue: `#104573`
- Grey: `#808184`
- Light Blue: `#1C93D1`

Updated in `flutter/lib/common.dart`:
- `accent` -> `#1C93D1` (Light Blue)
- `accent50` -> `#1C93D1` at 47% opacity
- `accent80` -> `#1C93D1` at 67% opacity
- `idColor` -> `#1C93D1` (Light Blue)
- `button` -> `#104573` (Dark Blue)
- Light theme `colorScheme.primary` -> `#104573` (Dark Blue)
- Dark theme `colorScheme.primary` -> `#1C93D1` (Light Blue)
- About dialog background -> `#104573` (Dark Blue)

### Build and Packaging
- Created `res/metroid-rs.desktop` (renamed from `rustdesk.desktop`)
- Created `res/metroid-rs-link.desktop` (renamed from `rustdesk-link.desktop`)
- Created `res/metroid-rs.service` (renamed from `rustdesk.service`)
- Updated `res/rpm.spec` with Metroid branding and paths
- Updated `res/msi/preprocess.py` defaults (app-name, manufacturer)
- Updated `res/msi/Package/Language/Package.en-us.wxl` installer strings

### URL Scheme
- Changed from `rustdesk://` to `metroid-rs://`

### Bundle Identifiers
- Changed from `com.carriez.rustdesk` / `com.carriez.flutter_hbb` to `com.metroid.remotesupport`

## URLs Retained (for future replacement)

The following rustdesk.com URLs are kept as-is and should be replaced when Metroid equivalents are ready:

- `flutter/lib/desktop/pages/desktop_setting_page.dart:2338` - privacy URL (`https://rustdesk.com/privacy.html`)
- `flutter/lib/desktop/pages/desktop_setting_page.dart:2346` - website URL (`https://rustdesk.com`)
- `flutter/lib/desktop/pages/desktop_home_page.dart:440` - download URL
- `flutter/lib/desktop/pages/desktop_home_page.dart:456` - GitHub releases URL
- `flutter/lib/mobile/pages/settings_page.dart:38` - website URL constant
- `flutter/lib/mobile/pages/settings_page.dart:968` - privacy URL
- `flutter/lib/mobile/pages/settings_page.dart:1081` - website URL
- `flutter/lib/desktop/pages/connection_page.dart:44` - pricing URL
- `flutter/lib/desktop/pages/install_page.dart:190` - privacy URL
- `flutter/lib/common.dart:3658` - website URL
- `libs/hbb_common/src/config.rs:89-92` - docs and wiki URLs

## AGPL Compliance

- Original Purslane Ltd copyright notices preserved in all files
- "Powered by RustDesk" attribution string retained (excluded from auto-replacement in `src/lang.rs`)
- About dialog shows both Metroid and RustDesk copyrights
- `NOTICE` file created at repo root
- `[lib] name = "librustdesk"` kept unchanged to maintain FFI compatibility
