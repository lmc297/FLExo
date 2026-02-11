# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-02-11

### Changed

- Changed underlying FLExo CRF (which was originally trained on a combination of multi- and single-gene exotoxins) to a completely new CRF, trained on multi-gene exotoxins only (this was done because the original CRF produced a ton of false positives, treating e.g., accessory genes within multi-gene exotoxin clusters as single-gene hits)

## [0.1.2] - 2025-08-14

### Fixed

- Fixed version number in __init__.py to correct value.

## [0.1.1] - 2025-08-14

### Added

- Created `CHANGELOG.md`

### Changed

- Changed default for `--cds` to `1` (originally `--cds 3`); `--cds 1` was used to perform all analyses in the preprint.

## [0.1.0] - 2025-08-14

### Added

- Initial release.

