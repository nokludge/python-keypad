#!/bin/bash

install() {
  echo "..."
}

test() {
  python -m unittest discover -s tests -p "Test*.py"
}

case "$1" in
  install) install;;
  test) test;;
  *) echo "Usage of $0 [ install | test ]"
esac