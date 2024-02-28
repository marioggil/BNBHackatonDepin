from pydal import DAL, Field
db = DAL("sqlite://db/storage.db")

db.define_table(
    "person",
    Field("name"),
    Field("age", type="integer")
)