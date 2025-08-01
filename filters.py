import sys
from datetime import datetime
from typing import List, Dict, Any, Optional


def filter_by_date(data: List[Dict[str, Any]], date_str: Optional[str]) -> List[Dict[str, Any]]:
    """Фильтрует данные по дате."""
    if not date_str:
        return data
    
    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print(f"Неверный формат даты: {date_str}. Используйте формат YYYY-MM-DD")
        sys.exit(1)
    
    filtered_data = []
    for item in data:
        timestamp = item.get('@timestamp')
        if timestamp:
            try:
                item_date = datetime.fromisoformat(timestamp.replace('Z', '+00:00')).date()
                if item_date == target_date:
                    filtered_data.append(item)
            except ValueError:
                continue
    
    return filtered_data 