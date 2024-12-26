# python-misc
Some random python code

### Transformers chat with SmolLM of Hugging Face

Build and run the Docker image

```bash
# Build the Docker image
docker build --pull --rm -f "Dockerfile" -t transformers_chat:latest "."

# Run the Docker container
docker run --rm transformers_chat
```

But the result is quite weird:

```
Oh, I'm so sorry to hear that. I'm so sorry, I'm so sorry. I'm so sorry. I'm so sorry. I'm so sorry. I'm so sorry. I'm so sorry. I'm so sorry. I'm so sorry. I'm so sorry...

Elapsed time: 74.3446478843689s | Memory footprint: 538.06 MB
```
