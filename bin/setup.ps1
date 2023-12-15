$binDir = (Get-Item $MyInvocation.MyCommand.Path).DirectoryName
$rootDir = (Get-Item $binDir).Parent.FullName
Set-Location $rootDir

$pythonVer = New-Object System.Version(3, 11, 6)
Write-Output ("Python=={0}" -f $pythonVer)

$nuGetExe = Join-Path $binDir "nuget.exe"
$pythonDir = Join-Path $binDir "python"
$pythonPath = Join-Path $pythonDir "tools\python.exe"


function InstallPython {
    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $nuGetExe
    $psi.Arguments = "install python -Version {0} -ExcludeVersion -OutputDirectory ""{1}""" -f $pythonVer.ToString(3), $binDir
    $psi.UseShellExecute = $false
    $psi.CreateNoWindow = $false
    $p = [System.Diagnostics.Process]::Start($psi)
    $p.WaitForExit()
}


if (Test-Path $pythonDir) {
    Remove-Item $pythonDir -Recurse -Force
}

InstallPython
Write-Output "Installed Python"
