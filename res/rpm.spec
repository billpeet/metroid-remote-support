Name:       metroid-rs
Version:    1.4.5
Release:    0
Summary:    Metroid Remote Support
License:    GPL-3.0
URL:        https://metroid.net.au
Vendor:     Metroid Electrical Engineering
Requires:   gtk3 libxcb libXfixes alsa-lib libva2 pam gstreamer1-plugins-base
Recommends: libayatana-appindicator-gtk3 libxdo

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/

%description
Metroid Remote Support - remote desktop software based on RustDesk.

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

%global __python %{__python3}

%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/metroid-rs/
mkdir -p %{buildroot}/usr/share/metroid-rs/files/
mkdir -p %{buildroot}/usr/share/icons/hicolor/256x256/apps/
mkdir -p %{buildroot}/usr/share/icons/hicolor/scalable/apps/
install -m 755 $HBB/target/release/metroid-rs %{buildroot}/usr/bin/metroid-rs
install $HBB/libsciter-gtk.so %{buildroot}/usr/share/metroid-rs/libsciter-gtk.so
install $HBB/res/metroid-rs.service %{buildroot}/usr/share/metroid-rs/files/
install $HBB/res/128x128@2x.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/metroid-rs.png
install $HBB/res/scalable.svg %{buildroot}/usr/share/icons/hicolor/scalable/apps/metroid-rs.svg
install $HBB/res/metroid-rs.desktop %{buildroot}/usr/share/metroid-rs/files/
install $HBB/res/metroid-rs-link.desktop %{buildroot}/usr/share/metroid-rs/files/

%files
/usr/bin/metroid-rs
/usr/share/metroid-rs/libsciter-gtk.so
/usr/share/metroid-rs/files/metroid-rs.service
/usr/share/icons/hicolor/256x256/apps/metroid-rs.png
/usr/share/icons/hicolor/scalable/apps/metroid-rs.svg
/usr/share/metroid-rs/files/metroid-rs.desktop
/usr/share/metroid-rs/files/metroid-rs-link.desktop
/usr/share/metroid-rs/files/__pycache__/*

%changelog
# let's skip this for now

%pre
# can do something for centos7
case "$1" in
  1)
    # for install
  ;;
  2)
    # for upgrade
    systemctl stop metroid-rs || true
  ;;
esac

%post
cp /usr/share/metroid-rs/files/metroid-rs.service /etc/systemd/system/metroid-rs.service
cp /usr/share/metroid-rs/files/metroid-rs.desktop /usr/share/applications/
cp /usr/share/metroid-rs/files/metroid-rs-link.desktop /usr/share/applications/
systemctl daemon-reload
systemctl enable metroid-rs
systemctl start metroid-rs
update-desktop-database

%preun
case "$1" in
  0)
    # for uninstall
    systemctl stop metroid-rs || true
    systemctl disable metroid-rs || true
    rm /etc/systemd/system/metroid-rs.service || true
  ;;
  1)
    # for upgrade
  ;;
esac

%postun
case "$1" in
  0)
    # for uninstall
    rm /usr/share/applications/metroid-rs.desktop || true
    rm /usr/share/applications/metroid-rs-link.desktop || true
    update-desktop-database
  ;;
  1)
    # for upgrade
  ;;
esac
