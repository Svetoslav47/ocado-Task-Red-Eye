#!/usr/bin/env python3

from typing import Tuple

EyePattern = Tuple[str, str, str, str, str]

eyePatterns = []


# zashto gi razmeni ve baluk?
EYE_PATTERN_1: EyePattern = (
  "/---\\",
  "| | |",
  "|-q-|",
  "| | |",
  "\\---/"
)

EYE_PATTERN_2: EyePattern = (
  "/---\\",
  "| | |",
  "| 0 |",
  "| | |",
  "\\---/"
)

EYE_PATTERN_3: EyePattern = (
  "/---\\",
  "|   |",
  "|-o-|",
  "|   |",
  "\\---/"
)


EYE_PATTERN_4: EyePattern = (
  "/---\\",
  "|\\ /|",
  "| w |",
  "|/ \\|",
  "\\---/"
)

eyePatterns = [EYE_PATTERN_1, EYE_PATTERN_4, EYE_PATTERN_3, EYE_PATTERN_2]