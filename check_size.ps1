$path = "E:\Documents\Geeky\Flutter\flutter_3.27.4.zip"
if (Test-Path $path) {
    $f = Get-Item $path
    $sizeMB = [math]::Round($f.Length / 1MB, 1)
    Write-Output "Size: $sizeMB MB"
} else {
    Write-Output "Not yet created"
}
