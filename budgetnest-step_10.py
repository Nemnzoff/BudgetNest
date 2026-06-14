# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: BudgetNest
class SearchFilter:
    def __init__(self, data):
        self.data = data
    
    def search(self, query):
        if not query.strip():
            return list(self.data)
        
        q_lower = query.lower()
        results = []
        
        for item in self.data:
            searchable_fields = ['name', 'category', 'goal_name']
            
            match_found = False
            
            for field in searchable_fields:
                if hasattr(item, field):
                    value = getattr(item, field)
                    if isinstance(value, str) and q_lower in value.lower():
                        match_found = True
                        break
                
                elif isinstance(value, dict) and 'name' in value:
                    if q_lower in value['name'].lower():
                        match_found = True
                        break
            
            if match_found or (hasattr(item, 'id') and str(item.id).lower().find(q_lower) != -1):
                results.append(item)
        
        return results
