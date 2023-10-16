# lst-pressure

Python module for calculating LST pressure based on scheduled observations

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Motivation](#motivation)
  - [Design](#design)
- [Usage](#usage)
  - [Installation](#installation)
  - [API](#api)
- [Local development](#local-development)
  - [Testing](#testing)
  - [Publishing](#publishing)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Motivation

Observation blocks encompass various time-related constraints, notably the Local Sidereal Time (LST) and some constraints related to UTC. As LST and UTC time can diverge over a year, it can be hard to quickly identify candidate UTC times based on LST ranges in conjunction with constraints related to sun/UTC.

This library should facilitate quickly generating a list of UTC ranges that satisfy observation-related constraints, and can be used to determine "potential lst-pressure" and "lst-pressure"

**_Potential LST-pressure_**: UTC periods that are potentially oversubscribed to observations, based on the number of observations that can be scheduled on a particular day

**_LST-pressure_**: UTC periods that are oversubscribed to observations that cannot be rescheduled to other slots

## Design

Each UTC day includes intervals in which an observation can be scheduled. These intervals are called:

- `AVOID_SUNRISE`
- `AVOID_SUNSET`
- `NIGHT_ONLY`
- `ALL_DAY`

Start by expanding a list of `N` days into a list of all possible intervals per day (i.e. each day includes 4 intervals). By creating an [interval tree](https://en.wikipedia.org/wiki/Interval_tree) from this list we can then easily identify UTC intervals that envelop some query (i.e. an lst interval). Or in other words, for an observation's required LST range we can easily query for UTC intervals that can support the LST range constraint over the `N` day period. The `UNION` of all candidate UTC intervals that all observations could be scheduled represents _potential LST-pressure_ over the `N` day period.

This list can then be processed (TODO) to determine _LST-pressure_ and in general help to inform scheduling of the MeerKAT telescope.

```txt
utc_intervals = ( N days ).map(day => {
  stats = sun_stats(day)
  AVOID_SUNRISE = {"name": "AVOID_SUNRISE", "interval": stats.calc(...)}
  AVOID_SUNSET = {"name": "AVOID_SUNSET", "interval": stats.calc(...)}
  NIGHT_ONLY = {"name": "NIGHT_ONLY", "interval": stats.calc(...)}
  ALL_DAY = {"name": "ALL_DAY", "interval": stats.calc(...)}
  return [AVOID_SUNRISE AVOID_SUNSET NIGHT_ONLY ALL_DAY]
}).flat()

idx = Idx(utc_intervals)

potential_lst_pressure = observations.map(o => {
  interval = [o.lst_start, o.lst_end]
  constraints = o. ...
  candidate_slots = idx.search(interval).filter(i => constraints(i))
  return candidate_slots
})

lst_pressure = deduplicate_candidate_slots(potential_lst_pressure)
```

# Usage

## Installation

Install the package from [PyPi](https://pypi.org/project/lst-pressure/)

```sh
pip install lst-pressure
```

## API

```python
from lst_pressure import Idx

idx = Idx()

for item in some_list:
  begin = item.get('begin')
  end = item.get('end')
  idx.insert(begin, end, item)

# Get all items that are contained in some interval
idx.find_enveloping(start, end)

# Get all items that are contain some interval
idx.find_overlapping(start, end)
```

# Local development

Ensure that you have Python v3.8.10 installed on your system, and then initiate the repository for local development with the following commands:

```sh
source env.sh
pipenv install
```

## Testing

To test the codebase, run `pytest` in the terminal. For live testing, use the [`chomp`](https://github.com/guybedford/chomp#install) task runner. Install either via Cargo (Rust), or via NPM (Node.js)

```sh
source env.sh
chomp --watch
```

## Publishing

The publish workflow is described in [.github/workflows/publish.yml](.github/workflows/publish.yml), and is triggered on pushes to the `release` branch. The published package is available on [PyPI](https://pypi.org/project/lst-pressure/). Make sure to first increment the version in [setup.py](./setup.py) before pushing to the release branch.
