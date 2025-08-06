#!/bin/bash


# Get current date for log filename
DATE=$(date +%F)
PROCESS_LOG="process_log_$DATE.log"
HIGH_MEM_LOG="high_mem_processes.log"


echo “Running System Health Check..."


# 1. Log Running Processes
echo "Logging all running processes to $PROCESS_LOG..."
ps aux > "$PROCESS_LOG"


# 2. Check for High Memory Usage more than 30%
echo "Checking for processes using more than 30% memory..."
HIGH_MEM_PROCESSES=$(ps aux --sort=-%mem | awk '$4 > 30')


if [ ! -z "$HIGH_MEM_PROCESSES" ]; then
    echo "WARNING: High memory usage detected!"
    echo "$HIGH_MEM_PROCESSES" >> "$HIGH_MEM_LOG"
fi


# 3. Checking Disk Usage on Root 
echo " Checking disk usage on root partition..."
DISK_USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')


if [ "$DISK_USAGE" -gt 80 ]; then
    echo "⚠️ WARNING: Disk usage on / is above 80% ($DISK_USAGE%)"
fi


# 4. Displaying Summary- combining all the 3 Questions 
TOTAL_PROCESSES=$(ps aux | wc -l)
HIGH_MEM_COUNT=$(echo "$HIGH_MEM_PROCESSES" | wc -l)


echo ""
echo "--- System Health Summary ---"
echo "Total running processes: $TOTAL_PROCESSES"
echo "Processes using >30% memory: $HIGH_MEM_COUNT"
echo "Disk usage on /: $DISK_USAGE%"
echo " Check complete."