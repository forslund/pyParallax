# pyParallax

A Simple parallax-scrolling library for pyGame.

It's simple, and I mean really simple. It lets you add a series of surfaces and scroll them at different speeds on top of each other. This gives a simple parallax effect that give a sense of depth.

## Usage

The class `ParallaxSurface` acts as a pygame surface container automatically scrolling it's subsurfaces at different speeds according to it's settings.

To add a surface there are several `add_*` methods to add a surface along with a `scroll_factor`. The scroll factor will indicate how much slower a surface should be scrolled, a higher factor will result in a slower scroll. The slower a surface is scrolled the further back it seems to be.

```python
# clouds should not move at all
bg.add(join(cloud_image, inf)
# shrubs should pan 3x as fast as the mountains
bg.add(join(mountains_image, 3)
bg.add(join(ground_and_shrubs_image, 1)
```

Simplest of these, `add()` takes an image as input and creates surfaces automatically.

If you'd like to add an image that does not scroll at all, set the `scroll_factor` for the image to `math.inf` when calling `ParallaxSurface.add()`. Due to how Python treats `math.inf`, an image with this `scroll_factor` will never scroll.

For more information checkout the help section

```python
>>> import parallax
>>> help(parallax.parallax)
```

## Example code

In the demo folder a simple demo is located. To run this From the root
directory, run

```
python3 -m demo.demo
```

## Contributors

Some people have helped to improve this small simple module. Thank you!

These awesome people are:

- zero-clouds
- ghighi-du63000
- williamu32
- cheffley6
