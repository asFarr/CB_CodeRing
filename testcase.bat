@echo off
set LOGFILE=test/batch.log
call :LOG > %LOGFILE%
exit /B

:LOG
echo  - Test Case 0 - No flags
python -m ring
echo  - Test Case 1 - -a
python -m ring -a
echo  - Test Case 2 - -h
python -m ring -h
echo " - Test Case 3 - -{e|d}(i:o:)t"
echo enc:
python -m ring -e -i test/input.txt -o test/enc/case03.txt -t
echo dec:
python -m ring -d -i test/enc/case03.txt -o test/dec/case03.txt -t
echo " - Test Case 4 - -{e|d}(i:o:)b"
echo enc:
python -m ring -e -i test/VBCABLE_Setup_x64.exe -o test/enc/case04.bin -b
echo dec:
python -m ring -d -i test/enc/case04.bin -o test/dec/case04.exe -b
echo " - Test Case 5 - -s{e|d}(i:o:)t"
echo enc:
python -m ring -e -i test/input.txt -o test/enc/case05.txt -t
echo dec:
python -m ring -d -i test/enc/case05.txt -o test/dec/case05.txt -t
echo " - Test Case 6 - -s{e|d}(i:o:)b"
echo enc:
python -m ring -se -i test/VBCABLE_Setup_x64.exe -o test/enc/case06.bin -b
echo dec:
python -m ring -sd -i test/enc/case06.bin -o test/dec/case06.exe -b