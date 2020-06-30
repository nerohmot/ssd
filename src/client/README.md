# src/client

The client side of `ssd` is a plugin for Spyder (V5 onward)

It provides 2 GUI elements:

- Toolbar : This indicates where the current project is executing.

- Connection Dialog : 

It also provedes a zeroconf 'listener', so that even if there is no [avahi](https://www.avahi.org/), [bonjour](https://en.wikipedia.org/wiki/Bonjour_(software)) or similar thing running on the network, things still work!
