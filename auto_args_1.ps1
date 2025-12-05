# Declare params
param(
    [string]
    $script_name = ".\tn_distance.py",
    
    [string]
    $output_file = "results\all_results.txt"
)

$ind_out_files = "results\result_"

$script_args = @(
    ("-file", "data\triangular_numbers_a100_l1_r100.txt"),
    ("-file", "data\triangular_numbers_a100_l1_r100.txt", "-precision", "100"),
    ("-file", "data\triangular_numbers_a100_l1_r1000.txt"),
    ("-file", "data\triangular_numbers_a100_l1_r1000.txt", "-precision", "100"),
    ("-file", "data\triangular_numbers_a100_l1_r10000.txt"),
    ("-file", "data\triangular_numbers_a100_l1_r10000.txt", "-precision", "100"),
    
    ("-file", "data\triangular_numbers_a1000_l1_r100.txt"),
    ("-file", "data\triangular_numbers_a1000_l1_r100.txt", "-precision", "100"),
    ("-file", "data\triangular_numbers_a1000_l1_r1000.txt"),
    ("-file", "data\triangular_numbers_a1000_l1_r1000.txt", "-precision", "100")
)

# Run each preset command and save results to file 
for ($i = 0; $i -lt $script_args.Count; $i++) {
    $res = python $script_name $script_args[$i]

    # ($script_args[$i] + "`r`n") | Out-File $output_file -Append -NoNewLine
    ($res + "`n") | Out-File $output_file -Append
    
    $res | Out-File ($ind_out_files + $i + ".txt")
}

# .\auto_args.ps1 -script_name .\tn_average_error.py