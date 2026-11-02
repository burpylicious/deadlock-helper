
from deadlock_helper.scaling import scaled_value

flog_base_damage = 65.0
flog_stat_scale = 0.85

print(scaled_value(flog_base_damage, 0, flog_stat_scale))
print(scaled_value(flog_base_damage, 20, flog_stat_scale))
print(scaled_value(flog_base_damage, 50, flog_stat_scale))
print(scaled_value(flog_base_damage, 100, flog_stat_scale))