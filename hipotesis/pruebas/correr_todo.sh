#!/bin/sh
# correr_todo.sh — corre los scripts de hipotesis/pruebas/ y guarda cada salida en salidas/<script>.txt
cd "$(dirname "$0")"
for s in testGeom testB1b dh mertens341 mobius field_signature arch_window rigorous_chain rho_interval castelnuovo gram bridge \
         blocks fejer_check balance fibres dedekind offline zeroside sweep circle_and_detect orbita_cert w4exact \
         corrected_operator law_resolution classes_test t1_index t2_loo euler_link teich escala_ceros_bajos \
         amplitud_clausula_ii kisin fermat_quintic_points; do
  t0=$(date +%s)
  python3 -I -u $s.py > salidas/$s.txt 2>&1
  echo "$s: salida $? en $(( $(date +%s) - t0 )) s"
done
