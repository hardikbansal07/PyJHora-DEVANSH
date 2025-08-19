import argparse
import json
from jhora.horoscope.main import Horoscope
from jhora.panchanga import drik


def _parse_args():
    parser = argparse.ArgumentParser(description="Compute horoscope information and output JSON.")
    parser.add_argument("--place", help="Place name including country code", default=None)
    parser.add_argument("--latitude", type=float, help="Latitude in decimal degrees")
    parser.add_argument("--longitude", type=float, help="Longitude in decimal degrees")
    parser.add_argument("--timezone", type=float, help="Timezone offset from UTC in hours")
    parser.add_argument("--date", required=True, help="Birth date in YYYY-MM-DD format")
    parser.add_argument("--time", required=True, help="Birth time in HH:MM or HH:MM:SS format")
    parser.add_argument("--ayanamsa", default="TRUE_CITRA", help="Ayanamsa mode")
    parser.add_argument("--language", default="en", help="Language code")
    return parser.parse_args()


def main():
    args = _parse_args()
    year, month, day = map(int, args.date.split("-"))
    date_obj = drik.Date(year, month, day)
    horoscope = Horoscope(
        place_with_country_code=args.place,
        latitude=args.latitude,
        longitude=args.longitude,
        timezone_offset=args.timezone,
        date_in=date_obj,
        birth_time=args.time,
        ayanamsa_mode=args.ayanamsa,
        language=args.language,
    )
    info, charts, ascendants = horoscope.get_horoscope_information()
    result = {
        "horoscope_info": info,
        "horoscope_charts": charts,
        "horoscope_ascendant_houses": ascendants,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
