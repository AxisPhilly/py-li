#py-li

A thin Python wrapper for the City of Philadelphia [Licenses and Inspections API](http://phlapi.com/licenseapi.html)

## Installation

Users:

    pip install py-li

Developers

    git clone git://github.com/axisphilly/py-li.git
    cd py-li
    mkvirtualenv venv
    pip install -r requirements.txt
    python test.py

## Usage

    import li

Get the 1,000 most recent permits

    li.get_permits()

See the examples folder and `test.py` for more usage examples.

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new pull Request

Make sure you added test cases for your feature!

## Copyright

Copyright © AxisPhilly. See LICENSE for details.
