# === Stage 22: Add favorite records and quick favorite listing ===
# Project: BudgetNest
class FavoriteManager:
    def __init__(self, db):
        self.db = db

    def toggle_favorite(self, record_id):
        with self.db.cursor() as cur:
            cur.execute("SELECT is_fav FROM records WHERE id=?", (record_id,))
            row = cur.fetchone()
            if not row or row[0] == 1:
                cur.execute("UPDATE records SET is_fav=0 WHERE id=?", (record_id,))
            else:
                cur.execute("UPDATE records SET is_fav=1 WHERE id=?", (record_id,))
            self.db.commit()

    def get_favorites(self):
        with self.db.cursor() as cur:
            cur.execute("SELECT * FROM records WHERE is_fav=1 ORDER BY created_at DESC")
            return cur.fetchall()
