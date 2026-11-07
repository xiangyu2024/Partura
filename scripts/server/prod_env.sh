# PROD W01 (research/prod_W01/PLAN.md), server side: the environment of every PROD process.  A TEMPLATE: copy it to
# <Partura home>/tmp/prod_env.sh on each host (tmp/ is not synced); it sources that host's own tmp/c05_env.sh first (paths, python,
# GPU / memory settings, the daily-field leaves), exactly as tmp/c07_env.sh and tmp/c08_env.sh do, then sets the study.
#   cd <Partura home> && source tmp/prod_env.sh
#
# What is set here, and why it is the C08 P arm / C07 M setting:
#   PARTURA_C0X=PROD, PARTURA_STUDY_DIR=prod_W01   the study and its directory under research/ (partura/study.py)
#   PARTURA_RANK_FIRST=1, PARTURA_NEUTRAL_POWERS=1,2,3   the new ruler (rank first, then smooth; residual on controls, squares, cubes)
#   C06_CTRL_STRIKE=0.8                            the permissive audit's strike line (c06_check.py; laptop side sets it too)
#   PARTURA_R_ADDITIONS=1                          R takes a better-but-different variant in as a head (PLAN section 1; C08 as it ran had
#                                                  this off -- see partura/study.py r_additions).  Set 0 for C08-as-it-ran.
#   TMPDIR=$PARTURA_HOME/tmp/sys_tmp               PROD only: temp files of python / numpy / torch go to the data disk, not the (small) root
#                                                  partition (PLAN section 3: the new host's root partition is never written to)
# Nothing else here may differ between the two hosts.
_d=$(dirname "${BASH_SOURCE[0]:-$0}"); [ -f "$_d/c05_env.sh" ] || _d=tmp
source "$_d/c05_env.sh"
unset _d
export PARTURA_STUDY_DIR=prod_W01 PARTURA_C0X=PROD PARTURA_RANK_FIRST=1 PARTURA_NEUTRAL_POWERS=1,2,3 C06_CTRL_STRIKE=0.8 PARTURA_R_ADDITIONS=1
mkdir -p "${PARTURA_HOME:?}/tmp/sys_tmp" && export TMPDIR="$PARTURA_HOME/tmp/sys_tmp"
