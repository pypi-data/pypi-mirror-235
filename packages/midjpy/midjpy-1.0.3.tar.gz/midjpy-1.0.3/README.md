
# MIDJPy

The MIDJPy package provides a simple and efficient way to interact with the MIDJ API. Utilize the power of MIDJ with just a few lines of Python code in your applications.

## Prerequisites

To use this package, you need to have a [midj.app subscription](https://midj.app/pricing).

## Features

- Generate content with `generate` method.
- Fetch content using the trigger ID with `get_by_trigger` method.
- Generate a variation of content with `generate_variation` method.
- Upscale images with `upscale_image` method.

## Installation

To install the MIDJPy package, use pip:

```bash
pip install midjpy
```

## Usage

Start by importing and initializing the MIDJ class:

```python
from midjpy.midj import MIDJ

midj = MIDJ(authorization='YOUR_AUTHORIZATION_TOKEN')
```

### Methods

#### For Subscription Users

##### `generate(prompt)`

Generate content based on a provided prompt:

```python
response = midj.generate('Hello, world!')
print(response)
```

##### `generate_variation(index, trigger_id, msg_hash)`

Generate a variation of content:

```python
response = midj.generate_variation(1, 'trigger_id_here', 'msg_hash_here')
print(response)
```

##### `upscale_image(index, trigger_id, msg_hash)`

Upscale an image:

```python
response = midj.upscale_image(1, 'trigger_id_here', 'msg_hash_here')
print(response)
```

#### For Pre-paid Users

##### `pregenerate(prompt)`

Generate content based on a provided prompt:

```python
response = midj.pregenerate('Hello, world!')
print(response)
```

##### `pregenerate_variation(index, trigger_id, msg_hash)`

Generate a variation of content:

```python
response = midj.pregenerate_variation(1, 'trigger_id_here', 'msg_hash_here')
print(response)
```

##### `preupscale_image(index, trigger_id, msg_hash)`

Upscale an image:

```python
response = midj.preupscale_image(1, 'trigger_id_here', 'msg_hash_here')
print(response)
```

#### Common API

##### `get_by_trigger(trigger_id)`

Fetch generated content by its trigger ID:

```python
response = midj.get_by_trigger('trigger_id_here')
print(response)
```

### Configuration

The `MIDJ` constructor accepts a configuration dictionary:

```python
config = {
    'baseURL': 'https://api.midj.app',  # Optional. This is the default.
    'authorization': 'YOUR_AUTHORIZATION_TOKEN'  # Required.
}

midj = MIDJ(config)
```

> ⚠️ Always keep your authorization token secret. Do not expose it in client-side code.

### Error Handling

All methods return an error object in case of any issues:

```python
response = midj.generate('Hello, world!')

if 'error' in response:
    print('Error:', response['error'])
else:
    print('Generated Content:', response)
```

## Contributing

For any bugs or feature requests, please open an issue on GitHub.

Please replace `'YOUR_AUTHORIZATION_TOKEN'` with your actual MIDJ API authorization token.