pkgname = "quickshell"
pkgver = "0.2.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCRASH_REPORTER=off",
    "-DDISTRIBUTOR=chimera",
    "-DHYPRLAND=off",
    "-DINSTALL_QML_PREFIX=lib/qt6/qml",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "cli11",
    "jemalloc-devel",
    "linux-pam-devel",
    "pipewire-devel",
    "qt6-qtbase-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtshadertools",
    "spirv-tools",
    "wayland-devel",
    "wayland-progs",
    "wayland-protocols",
]
depends = [
    "cmake",
    "pipewire-libs",
    "qt6-qtbase",
    "qt6-qtdeclarative",
    "wayland",
]
pkgdesc = "Flexible QtQuick based desktop shell toolkit"
license = "LGPL-3.0-only"
url = "https://quickshell.org"
source = f"https://github.com/quickshell-mirror/quickshell/archive/refs/tags/v{pkgver}.zip"
sha256 = "1544fa6755a271be041b8a854beb94f9e780e51185acd3f2e9252c0c49642cbd"
