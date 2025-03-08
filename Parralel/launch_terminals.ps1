# Get all CSV files in the csv_splits directory
$csvFiles = Get-ChildItem -Path .\csv_splits -Filter "csv_*.csv"

foreach ($csvFile in $csvFiles) {
    $fullPath = ".\csv_splits\$($csvFile.Name)"
    Write-Host "Launching terminal for: $fullPath"
    
    try {
        Start-Process cmd -ArgumentList "/k conda activate base && python gen.py $fullPath"
        Start-Sleep -Milliseconds 500  # Add small delay between launches
    }
    catch {
        Write-Host "Failed to launch terminal for: $fullPath"
        Write-Host "Error: $_"
    }
} 