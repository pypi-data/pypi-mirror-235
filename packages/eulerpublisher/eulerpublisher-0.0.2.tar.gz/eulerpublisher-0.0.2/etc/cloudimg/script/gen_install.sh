#!/bin/bash
set -e

# mount disk
DEV_NUM="/dev/nbd0"
OPENEULER_IMG="$1"
OUTPUT_IMG_NAME="$2"
TMP_DATA_PATH="$3"
INSTALL_PACKAGES="$4"
MOUNT_DIR="/mnt/nbd0"
OUTPUT_DIR="/etc/eulerpublisher/cloudimg/gen/output/"
sudo mkdir -p $OUTPUT_DIR

if [[ $(uname) == "Darwin" ]]; then
    echo "MacOS is not supported"
    exit 1
fi

sudo modprobe nbd max_part=3
nbd_mount=$(mount | grep nbd0 || echo -n "")
if [[ ! -z "${nbd_mount}" ]]; then
    sudo umount "${MOUNT_DIR}"
fi

nbd_loaded=$(lsblk | grep nbd0 || echo -n "")
if [[ ! -z "${nbd_loaded}" ]]; then
    sudo qemu-nbd -d "${DEV_NUM}"
fi
sudo qemu-nbd -c "${DEV_NUM}" "${TMP_DATA_PATH}${OPENEULER_IMG}"
sleep 3

# change configuration
sudo mkdir -p ${MOUNT_DIR}
sudo mount ${DEV_NUM}p2 ${MOUNT_DIR}
sleep 3

# the packages must be installed
yum -y --installroot=${MOUNT_DIR} install cloud-init cloud-utils-growpart gdisk
# other packages need to be installed
yum -y --installroot=${MOUNT_DIR} install $(cat ${INSTALL_PACKAGES})

# for security
set +e
chmod -f 400 ${MOUNT_DIR}/etc/ssh/*key
chown -f -R root:root ${MOUNT_DIR}/etc/ssh/*key.pub

set -e
sudo sed -i "/MACs/d"                                        ${MOUNT_DIR}/etc/ssh/sshd_config
sudo sed -i '$a\MACs hmac-sha2-512,hmac-sha2-256'            ${MOUNT_DIR}/etc/ssh/sshd_config
sudo sed -i "/Ciphers/d"                                     ${MOUNT_DIR}/etc/ssh/sshd_config
sudo sed -i '$a\Ciphers aes256-ctr,aes192-ctr,aes128-ctr'    ${MOUNT_DIR}/etc/ssh/sshd_config

# disable PermitRootLogin
sudo sed -i '/PermitRootLogin/s/^/# /'                       ${MOUNT_DIR}/etc/ssh/sshd_config
sudo sed -i '$a\PermitRootLogin no'                          ${MOUNT_DIR}/etc/ssh/sshd_config

sudo sync
sleep 3
sudo umount ${MOUNT_DIR}
sudo qemu-nbd -d $DEV_NUM
qemu-img convert -O ${OUTPUT_IMG_NAME##*.} ${TMP_DATA_PATH}${OPENEULER_IMG} ${OUTPUT_DIR}${OUTPUT_IMG_NAME}
