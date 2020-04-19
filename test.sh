#!/usr/bin/env bash

TIMEFORMAT="%Rs"
src_file="/bin/gethostip"
declare -A enc_files=([2]="tool.b2" [7]="tool.b7" [16]="tool.b16" [32]="tool.b32"
                      [64]="tool.b64" [74]="tool.b74" [81]="tool.b81" [94]="tool.b94")
declare -A dec_files=([2]="tool.2" [7]="tool.7" [16]="tool.16" [32]="tool.32"
                      [64]="tool.64" [74]="tool.74" [81]="tool.81" [94]="tool.94")

for base in "${!enc_files[@]}"; do
    echo "Convert ${src_file} to base${base} (${enc_files[$base]}):"
    echo -en "\ttime: "
    time ./base94.py -e "${src_file}" "${enc_files[$base]}" ${base}
    src_size="$(stat -c '%s' "${src_file}")"
    dst_size="$(stat -c '%s' "${enc_files[$base]}")"
    over_size="$((dst_size - src_size))"
    echo -e "\tsize: ${src_size}b -> ${dst_size}b (+${over_size}b / $(( over_size*100/src_size ))%)"
done

echo

for base in "${!dec_files[@]}"; do
    echo -n "Convert from base${base} to origin (${dec_files[$base]}): "
    time ./base94.py -d "${enc_files[$base]}" "${dec_files[$base]}" ${base}
done

echo -e "\nVerify sha256 check sums after conversions:"
sha256sum -b "${src_file}" "${dec_files[@]}"
