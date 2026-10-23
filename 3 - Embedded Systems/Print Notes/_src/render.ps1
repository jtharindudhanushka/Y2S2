# Usage: powershell -File render.ps1 lesson04 "Lesson 04 - Polling and Interrupts"
param([string]$src, [string]$name)
$edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$out = Join-Path (Split-Path -Parent $here) "$name.pdf"
$url = "file:///" + ($here.Replace('\', '/').Replace(' ', '%20')) + "/$src.html"
Remove-Item $out -ErrorAction SilentlyContinue
Start-Process -FilePath $edge -Wait -NoNewWindow -ArgumentList @("--headless=new", "--disable-gpu", "--no-first-run", "--user-data-dir=$env:TEMP\edge_pdf_profile", "--no-pdf-header-footer", "--print-to-pdf=`"$out`"", "`"$url`"") 2>$null
Write-Output $out
