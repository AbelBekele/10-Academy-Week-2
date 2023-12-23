select *
from {{ ref('trajectory') }} t
inner join {{ ref('type_distribution') }} td on t.id = td.id
where t.id = 1