function CopyPrebuiltDLLs () {
    $target = "x86"
    if ($env:PYTHON_ARCH -eq "64") {
        $target = "x64"
    }
    $prebuilt_dir = "prebuilt-"+$target

    $basedir = $pwd.Path + "\"
    $dlls = $basedir + $prebuilt_dir + "\" + "*.dll"
    $destpath = $basedir + "pygame"

    Copy-item $dlls -destination $destpath
}

function main () {
    CopyPrebuiltDLLs
}

main
