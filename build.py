"""Rebuild business-name-fit.skill from the business-name-fit/ source folder.

Run this after editing anything inside business-name-fit/, then commit the
regenerated .skill alongside your change:

    python build.py

Only the files the skill reads at runtime go into the bundle. The WIPO PDF in
references/ is deliberately excluded — nothing reads it and it is 1.6 MB.
"""

import os
import sys
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "business-name-fit")
OUT = os.path.join(ROOT, "business-name-fit.skill")

# Paths relative to business-name-fit/, in the layout SKILL.md expects.
INCLUDE = [
    "SKILL.md",
    "examples/worked-examples.md",
    "references/naming-research.md",
]


def main():
    missing = [r for r in INCLUDE
               if not os.path.isfile(os.path.join(SRC, r.replace("/", os.sep)))]
    if missing:
        sys.exit("error: missing source file(s): %s" % ", ".join(missing))

    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as bundle:
        for rel in INCLUDE:
            bundle.write(os.path.join(SRC, rel.replace("/", os.sep)),
                         "business-name-fit/" + rel)

    print("wrote %s" % os.path.basename(OUT))
    with zipfile.ZipFile(OUT) as bundle:
        for info in bundle.infolist():
            print("  %7d  %s" % (info.file_size, info.filename))


if __name__ == "__main__":
    main()
