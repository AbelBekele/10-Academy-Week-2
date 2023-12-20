CREATE TABLE IF NOT EXISTS automobiles
(
    "id" SERIAL NOT NULL,
    "track_id" TEXT NOT NULL,
    "lat" TEXT NOT NULL,
    "lon" TEXT DEFAULT NULL,
    "speed" TEXT DEFAULT NULL,
    "lon_acc" TEXT DEFAULT NULL,
    "lat_acc" TEXT DEFAULT NULL,
    "time" TEXT DEFAULT NULL,
    PRIMARY KEY ("id"),
    CONSTRAINT fk_traffic
        FOREIGN KEY("track_id") 
            REFERENCES traffic(track_id)
            ON DELETE CASCADE
    
);