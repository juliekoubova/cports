pkgname = "poppler"
pkgver = "24.08.0"
_test_commit = "ff3133cdb6cb496ee1d2c3231bfa35006a5e8410"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DENABLE_UNSTABLE_API_ABI_HEADERS=ON",
    "-DENABLE_BOOST=ON",
    "-DENABLE_CPP=ON",
    "-DENABLE_GLIB=ON",
    "-DENABLE_GOBJECT_INTROSPECTION=ON",
    "-DENABLE_NSS3=ON",
    "-DENABLE_UTILS=ON",
    # in contrib
    "-DENABLE_GPGME=OFF",  # creates a cycle
    "-DENABLE_QT5=OFF",
    "-DENABLE_QT6=OFF",
]
hostmakedepends = [
    "cmake",
    "glib-devel",
    "gobject-introspection",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "cairo-devel",
    "glib-devel",
    "lcms2-devel",
    "libcurl-devel",
    "libpng-devel",
    "libtiff-devel",
    "nss-devel",
    "openjpeg-devel",
]
pkgdesc = "PDF rendering library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://poppler.freedesktop.org"
source = [
    f"{url}/poppler-{pkgver}.tar.xz",
    f"https://gitlab.freedesktop.org/poppler/test/-/archive/{_test_commit}/test-{_test_commit}.tar.gz",
]
source_paths = [".", "testdata"]
sha256 = [
    "97453fbddf0c9a9eafa0ea45ac710d3d49bcf23a62e864585385d3c0b4403174",
    "98a06e7dd7619fe20bfd99505a31993dbe40517678d81278e6395a30a40f03bf",
]


def init_configure(self):
    self.configure_args.append(f"-DTESTDATADIR={self.chroot_srcdir}/testdata")


@subpackage("libpoppler")
def _lib(self):
    self.subdesc = "runtime library"
    self.depends = ["poppler-data"]

    return ["usr/lib/libpoppler.so.*"]


@subpackage("libpoppler-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libpoppler-cpp")
def _cpp_lib(self):
    self.subdesc = "C++ binding"

    return ["usr/lib/libpoppler-cpp.so.*"]


@subpackage("libpoppler-glib")
def _glib(self):
    self.subdesc = "GLib binding"

    return ["usr/lib/libpoppler-glib.so.*", "usr/lib/girepository-1.0"]
