import docker

def print_images(client):
    """
    Display the current list of images available on docker locally
    """
    images = client.images.list()
    for img in images:
        print(f"{img.id} - {img.tags}")


# ----------------------------------------------------------------------------

# The name of the image 'iterate-demo:iter-N'
image_name = "iterate-demo"

# We start with a basic file
print("Reading original file")
with open('src/original.txt') as fh:
    text = fh.read()
    print(text)

# Connect to local docker
client = docker.from_env()

# Make sure that we've pulled the `ubuntu` image - see `FROM` in `src/Dockerfile`:
client.images.pull('ubuntu:latest')

print("Images at start up:")
print_images(client)

# Simulate 10 iterations 
# At each iteration we write a new line into changing file
for i in range(0, 10):
    version = f'iter-{i}'
    tag = f"{image_name}:{version}"
    text = text + f"Added iteration {i}\n"

    #  Update the changing file 
    with open('src/changing-file.txt', 'w') as fh:
        fh.write(text)
    
    # Build the image using `src/Dockerfile`, giving it a new image
    print(f"Build: {tag}")
    #apiclient = docker.APIClient()
    client.images.build(path='src', tag=tag)

    # Can we see the new version?
    print_images(client)

    # Run the image
    print(f"Run ...")
    print(client.containers.run(tag))
    print(f"Run ... done")
