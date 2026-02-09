@echo off
set PATH=E:\Documents\Geeky\Flutter\flutter3\flutter\bin;%PATH%
set LIBCLANG_PATH=C:\Program Files\LLVM\bin
set VCPKG_ROOT=C:\vcpkg
cd /d E:\Documents\Geeky\Rust\rustdesk

echo === Step 1: Building Rust library with Flutter feature ===
cargo build --features flutter --lib --release
if errorlevel 1 (
    echo Rust library build failed!
    exit /b 1
)

echo === Step 2: Building Flutter Windows app ===
cd flutter
flutter build windows --release
if errorlevel 1 (
    echo Flutter build failed!
    exit /b 1
)

echo === Build complete ===
