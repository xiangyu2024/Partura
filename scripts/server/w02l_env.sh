# PROD W02L (research/prod_W02L/PLAN.md), server side: the environment of every W02L process.  A TEMPLATE: copy to
# <Partura home>/tmp/w02l_env.sh on the new host.  It is prod_env.sh (the W01 production environment) plus:
#   PARTURA_STUDY_DIR=prod_W02L, PARTURA_VIEW=w02          the study and the user's split of 2026-11-08 (2026 never in the view)
#   PARTURA_EXTRA_CONTROLS(_DATES)                         ruler B: the two champions join the neutral basis (PLAN section 3)
#   PARTURA_WAVE_BAN=1, PARTURA_SKELETON_BAN_FILE          one library ban for the wave + every library skeleton (section 4)
#   PARTURA_EXEMPLAR_CACHE(_GB)                            ban exemplars' rank fingerprints computed once, kept on disk
#   PARTURA_BASIS_CACHE, PARTURA_GP_CPU_FALLBACK=1      the neutral basis kept on disk; a search starts on the CPU when both GPU ways are taken
#   host caps / memory lines                               the 1 TB host: 12 run slots, 2 GPU ways (the card), panel cache 64 GB,
#                                                          machine-wide anonymous memory line 850 GB, 200 GB per process
_d=$(dirname "${BASH_SOURCE[0]:-$0}"); [ -f "$_d/prod_env.sh" ] || _d=tmp
source "$_d/prod_env.sh"
unset _d
C=runs/prod_W01/two_level/champions
export PARTURA_STUDY_DIR=prod_W02L PARTURA_VIEW=w02 \
  PARTURA_EXTRA_CONTROLS=$C/signal_手写库冠军_20260916.npy,$C/signal_挖掘冠军_20260916.npy PARTURA_EXTRA_CONTROLS_DATES=$C/two_level_forward_20260916.json \
  PARTURA_WAVE_BAN=1 PARTURA_SKELETON_BAN_FILE=$PARTURA_HOME/research/prod_W02L/library_all.json \
  PARTURA_EXEMPLAR_CACHE=$PARTURA_HOME/runs/_exemplar_cache PARTURA_EXEMPLAR_CACHE_GB=60 \
  PARTURA_HOST_SLOTS=12 PARTURA_HOST_GPU_WAYS=4 PARTURA_HOST_PANEL_CACHE_GB=64 PARTURA_PANEL_CACHE_GB=64 \
  PARTURA_CGROUP_LIMIT_GB=850 PARTURA_SELF_LIMIT_GB=200 \
  PARTURA_BASIS_CACHE=$PARTURA_HOME/runs/_basis PARTURA_GP_CPU_FALLBACK=1 PARTURA_GP_CPU_THREADS=6 \
  PARTURA_SLOT_NAME=w02lslot PARTURA_REPROMOTE=1 ALPHACUBE_BOUNDARY_MEMORY=1 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
  PARTURA_SLOTS=12 PARTURA_GPU_WAYS=3 PARTURA_GP_GPU_FRACTION=0.30 PARTURA_CORR_GPU_LOCK=gpucorr PARTURA_GPUCORR_WAYS=2 \
  PARTURA_LOCATE_SLOT_NAME=w02lloc PARTURA_LOCATE_GPU_LOCK=gpuloc PARTURA_GPULOC_WAYS=2
unset C
