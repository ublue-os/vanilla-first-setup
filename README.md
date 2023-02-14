# vanilla-first-setup
![Build Status](https://copr.fedorainfracloud.org/coprs/ublue-os/vanilla-first-setup/package/vanilla-first-setup/status_image/last_build.png?)

Copr build script for [Vanilla-OS/first-setup](https://github.com/Vanilla-OS/first-setup), for use with custom OCI images.

# Usage
    # Enable Copr repository
    wget https://copr.fedorainfracloud.org/coprs/ublue-os/vanilla-first-setup/repo/fedora-$(rpm -E %fedora)/ublue-os-vanilla-first-setup-fedora-$(rpm -E %fedora).repo -O /etc/yum.repos.d/_copr_ublue-os-vanilla-first-setup.repo
    
    # Install package
    rpm-ostree install vanilla-first-setup
    
    # Disable repository after including in your OCI
    sed -i 's@enabled=1@enabled=0@g' /etc/yum.repos.d/_copr_ublue-os-vanilla-first-setup.repo
