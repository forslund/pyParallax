pyParallax
====================

A Simple parallax-scrolling library for pyGame.

It's simple, and I mean really simple. It lets you add a series of surfaces and scroll them at different speeds on top of each other. This gives a simple parallax effect that give a sense of depth.

If you'd like to add an image that does not scroll at all, set the `scroll_factor` for the image to `math.inf` when calling `ParallaxSurface.add()`. Due to how Python treats `math.inf`, an image with this `scroll_factor` will never scroll.

How to run the demo
-------------------
From the root directory, run `python3 -m demo.demo`

Contributors:
-------------
zero-clouds  
ghighi-du63000  
williamu32  
cheffley6  
