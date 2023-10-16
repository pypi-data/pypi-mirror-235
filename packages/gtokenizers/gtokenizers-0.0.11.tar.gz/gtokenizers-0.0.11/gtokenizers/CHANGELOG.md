# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.11]
- introduced concept of `TokenizedRegion`.
- `TokenizedRegion`s contain and `id`, `bit_vector`, and `one_hot_vector`.
- `TokenizedRegion`s are yielded by `TokenizedRegionSet`s.
- Added more magic methods to `TokenizedRegionSet` to make it more pythonic.
- More unit tests.

## [0.0.10]
- added .pyi stubs for type hinting inside IDEs

## [0.0.9]
- Fix bug that prevented unknown tokens from being yielded when tokenizing region sets.

## [0.0.8]
- Initial release of the `TreeTokenizer`  for tokenizing traditional region sets (bed files).