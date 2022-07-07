hifiasm -o test -t1 -f0 ../../00.data/4.pacbio_CCS/test2.fa.gz 2> test.log
#awk '/^S/{print ">"$2;print $3}' test.bp.p_ctg.gfa > test.bp.p_ctg.fa

