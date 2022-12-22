import json
import argparse
import shutil, os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build the extension")
    parser.add_argument("-t", "--target", type=str, help="The target browser", choices=["firefox","chrome"], required=True)

    args = parser.parse_args()
    if os.path.exists("build"):
        shutil.rmtree("build")
    shutil.copytree("src", "build")
    with open("build/manifest.json","r+") as fp:
        manifest = json.load(fp)
        version = 3 if args.target == "chrome" else 2
        manifest["manifest_version"] = version
        fp.seek(0)
        json.dump(manifest, fp, indent=4)
        fp.truncate()
    shutil.make_archive("output/build", "zip", "build")