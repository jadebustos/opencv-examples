# Set your manifest name
export MANIFEST_NAME="multiarch-example"

# Set the required variables
export BUILD_PATH="amd64"
export REGISTRY="quay.io"
export USER="rhte_2019"
export IMAGE_NAME="example"
export IMAGE_TAG="v1"
export OPENCV_VERSION=4.5.5

# Create a multi-architecture manifest
buildah manifest create ${MANIFEST_NAME}

# Build your amd64 architecture container
buildah bud \
    --tag "${REGISTRY}/${USER}/${IMAGE_NAME}:${IMAGE_TAG}" \
    --manifest ${MANIFEST_NAME} \
    --build-arg OPENCV_VERSION=4.5.5 \
    --arch amd64 \
    ${BUILD_PATH}

# Build your arm64 architecture container
#buildah bud \
#    --tag "${REGISTRY}/${USER}/${IMAGE_NAME}:${IMAGE_TAG}" \
#    --manifest ${MANIFEST_NAME} \
#    --arch arm64 \
#    ${BUILD_PATH}

# Push the full manifest, with both CPU Architectures
buildah manifest push --all \
    ${MANIFEST_NAME} \
    "docker://${REGISTRY}/${USER}/${IMAGE_NAME}:${IMAGE_TAG}"
