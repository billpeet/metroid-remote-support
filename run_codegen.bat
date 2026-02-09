@echo off
set PATH=E:\Documents\Geeky\Flutter\flutter3\flutter\bin;%PATH%
set LIBCLANG_PATH=C:\Program Files\LLVM\bin
cd /d E:\Documents\Geeky\Rust\rustdesk
flutter_rust_bridge_codegen --rust-input ./src/flutter_ffi.rs --dart-output ./flutter/lib/generated_bridge.dart
