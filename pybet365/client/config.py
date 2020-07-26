"""Configuration File for Bet365 Client."""
from enum import DynamicClassAttribute, Enum

from typing import Union


class ExtendedEnum(Enum):
    """Allows access to overloaded functions for standard Enum"""

    @classmethod
    def list(cls):
        """Interface to provide all allowed values for a RundownSportId. """
        return list(map(lambda c: (c.sport_id, c.pretty), cls))


class Bet365SportId(ExtendedEnum):
    """
    Bet365 API SportId Enumeration.

    Registered members have accesses to:
    _name_ - name
    _value_ - value[0]
    _pretty_ - value[1]

    (e.g.)
    >>> soccer = Bet365SportId.AMERICAN_FOOTBALL

    >>> soccer.name
    >>> "AMERICAN_FOOTBALL"

    >>> soccer.value
    >>> 12

    >>> soccer.pretty
    >>> "american-football"
    """

    @DynamicClassAttribute
    def pretty(self) -> Union[str, None]:
        """Access for `pretty` in base `Enum`."""
        return self.value[1] if self else None

    @DynamicClassAttribute
    def sport_id(self) -> Union[str, None]:
        """Access for `sport_id` in base `Enum`."""
        return self.value[0] if self else None

    SOCCER = ("1", "soccer")
    CRICKET = ("3", "cricket")
    RUGBY_UNION = ("8", "rugby-union")
    BOXING_UFC = ("9", "boxing-ufc")
    AMERICAN_FOOTBALL = ("12", "american-football")
    TENNIS = ("13", "tennis")
    SNOOKER = ("14", "snooker")
    DARTS = ("15", "darts")
    BASEBALL = ("16", "baseball")
    ICE_HOCKEY = ("17", "ice-hockey")
    BASKETBALL = ("18", "basketball")
    RUGBY_LEAGUE = ("19", "rugby")
    AUSTRALIAN_RULES = ("36", "austalian-rules")
    BOWLS = ("66", "bowls")
    GAELIC_SPORTS = ("75", "gaelic-sports")
    HANDBALL = ("78", "handball")
    FUTSAL = ("83", "futsal")
    FLOORBALL = ("90", "floorball")
    VOLLEYBALL = ("91", "volleyball")
    TABLE_TENNIS = ("92", "table-tennis")
    BADMINTON = ("94", "badminton")
    BEACH_VOLLEYBALL = ("95", "beach-volleyball")
    SQUASH = ("107", "squash")
    WATER_POLO = ("110", "water-polo")
    E_SPORTS = ("151", "e-sports")


class Bet365Mnemonic(Enum):
    """
    Bet365 API Mnemonic Field Enumeration.
    see: (https://1394697259.gitbook.io/bet365-api/bet36)

    Internal mapping to cast fields where necessary
    """

    PLACE_365 = "3P"
    WIN_365 = "3W"
    MARKET_GROUP_PAIR_ID = "4Q"
    FINANCIALS_PRICE_1 = "AB"
    STATS_COLUMN = "AC"
    ADDITIONAL_DATA_TEAM_TOUCHDOWN_QUOTE = "AD"
    STATS_CELL = "AE"
    ARCHIVE_FIXTURE_INFO = "AF"
    ASIAN_HOVER_FINANCIALS_MARKET_ODDS_1 = "AH"
    ANIMATION_ID = "AI"
    FINANCIALS_MARKET_ODDS_2 = "AJ"
    ANIMATION_ICON = "AM"
    ANIMATION_TOPIC = "AO"
    STATS_PANE = "AP"
    FINANCIALS_CLOSE_TIME = "AQ"
    ADDITIONAL_STATS_ANIMATION_SOUND_TEAM_FIELDGOAL_QUOTE = "AS"
    ANIMATION_TEXT_STATS_TAB = "AT"
    AUDIO_AVAILABLE = "AU"
    ARCHIVE_VIDEO_AVAILABLE = "AV"
    BUTTON_BAR = "BB"
    BOOK_CLOSES_CLOSE_BETS_COUNT = "BC"
    PULL_BET_DATA = "BD"
    BET = "BE"
    BLURB_HEADER = "BH"
    BUTTON_BAR_INDEX_BUTTON_SPLIT_INDEX = "BI"
    BASE_LINE = "BL"
    BASE_ODDS_OPEN_BETS_COUNT = "BO"
    BANNER_STYLE = "BS"
    INFO_POD_DETAIL_2 = "BT"
    C1_ID_MINI_DIARY_C1 = "C1"
    C2_ID_MINI_DIARY_C2 = "C2"
    MINI_DIARY_C3 = "C3"
    CLOSE_BETS = "CB"
    BET_TYPE_PULL_COMPETITION_CODE = "CC"
    COMPETITION_DROPDOWN_FINANCIALS_TRADE = "CD"
    CONFIG = "CF"
    GLOBAL_CONFIG = "CG"
    CLASS_ID_MINI_DIARY_CUP_ICON = "CI"
    COMPETITION_KEY = "CK"
    CLASSIFICATION = "CL"
    BET_CALL_FEATURE_DISABLED_COMMENT = "CM"
    CHANNEL_COLUMN_NUMBER = "CN"
    COLUMN = "CO"
    CLOSE_BETS_PRESENTATION_PULL_DISABLED_CURRENT_PROGRESS_CURRENT_PERIOD = "CP"  # noqa: E501
    CLASS_ORDER_CLOSE_BET_RETURNS = "CR"
    CLASSIFICATIONS = "CS"
    COMPETITION_NAME = "CT"
    CURRENT_INFO = "CU"
    DATA_1 = "D1"
    DATA_2 = "D2"
    DATA_3 = "D3"
    DATA_4 = "D4"
    DATA_5 = "D5"
    DIARY_DAY = "DA"
    DISPLAY_CLOCK = "DC"
    DISPLAY_DATE = "DD"
    DESCRIPTION = "DE"
    IN_PLAY_LAUNCHER_DISPLAY_MODE = "DM"
    DIARY_NAME_DRAW_NUMBER = "DN"
    DEFAULT_OPEN = "DO"
    DECIMAL_PLACES = "DP"
    DIARY_REFRESH = "DR"
    DISPLAY_SCORE = "DS"
    DISABLE_COLUMN_DISTRIBUTION = "DX"
    DIARY = "DY"
    EVENT_TIME = "EA"
    ERROR_CODE_EXCLUDED_COUNTRY_CODES = "EC"
    EXTRA_DATA_2_TEAM_ODDS_A = "ED"
    ETOTE_LINK_DATA = "EE"
    EVENT_ID = "EI"
    EXTRA_STATS_AVAILABLE = "EL"
    EMPTY = "EM"
    EXTRA_PARTICIPANTS = "EP"
    ERROR_LOGGING = "ER"
    EMBEDDED_STREAMING_EXTRA_SCORES = "ES"
    END_TIME_EVENT_TYPE = "ET"
    EVENT = "EV"
    EACH_WAY = "EW"
    EXTRA_DATA_1_TEAM_ODDS_H = "EX"
    FORCE_DISPLAY = "FD"
    FILTERING = "FF"
    FIXTURE_PARENT_ID = "FI"
    FINANCIALS_FEED_1 = "FK"
    FINANCIALS_PERIOD_1_APN_FLUC = "FL"
    FINANCIALS_MARKET_1A = "FM"
    FINANCIALS_MARKET_1B = "FN"
    FINANCIALS_FEED_2_FORM_PULL = "FO"
    FINANCIALS_PERIOD_2_FIXED_PLACE = "FP"
    FINANCIALS_MARKET_2A = "FQ"
    FINANCIALS_MARKET_2B = "FR"
    FIXTURE_STARTED = "FS"
    FIXED_WIN = "FW"
    LOTTO_GAME_CODE = "GC"
    LOTTO_GAME_MARKET = "GM"
    GROUP = "GR"
    HANDICAP = "HA"
    HANDICAP_FORMATTED = "HD"
    HEADER_IMAGE_BET_HISTORY = "HI"
    MARKET_BAR = "HM"
    DEFAULT_OPEN_HOMEPAGE = "HO"
    SHOW_ON_HOMEPAGE = "HP"
    HASH = "HS"
    POD_HEADER_TEXT = "HT"
    INFO_BANNER_SUBHEAD2 = "HU"
    POD_BODY_TEXT_2 = "HV"
    HORSE_WEIGHT = "HW"
    HORSE_AGE = "HY"
    ID2 = "I2"
    AUDIO_ICON_DIARY_AUDIO_AVAILABLE = "IA"
    IBOX = "IB"
    ICON = "IC"
    ID = "ID"
    IN_PLAY = "IF"
    IMAGE_ID = "IG"
    IMAGE_INCLUDE_OVERVIEW_MARKET = "IM"
    INFO_INFO_POD_IMAGE_URL = "IN"
    ITEM_ORDER = "IO"
    IN_PLAY_AVAILABLE_FLAG_PARENT_ID = "IP"
    INFO_POD_IMAGE1 = "IQ"
    INRUNNING_INFO = "IR"
    INFO_POD_IMAGE_PATH1 = "IS"
    TOPIC_ID = "IT"
    INFO_POD_IMAGE2 = "IU"
    JOCKEY_PULL = "JN"
    JOCKEY = "JY"
    KIT_COLORS = "KC"
    KIT_ID = "KI"
    BREADCRUMB_LEVEL_1 = "L1"
    LABEL_INFO_POD_LINK_1_ID = "LA"
    INFO_POD_LINK_1_DISPLAY_TEXT = "LB"
    EVENT_COUNT_INFO_POD_LINK_1_C1_ID = "LC"
    INFO_POD_LINK_1_C1_ID_TABLE = "LD"
    INFO_POD_LINK_1_C2_ID = "LE"
    INFO_POD_LINK_1_C2_ID_TABLE = "LF"
    INFO_POD_LINK_2_ID_SOCCER_LEAGUE = "LG"
    INFO_POD_LINK_2_DISPLAY_TEXT = "LH"
    INFO_POD_LINK_2_C1_ID = "LI"
    INFO_POD_LINK_2_C1_ID_TABLE = "LJ"
    INFO_POD_LINK_2_C2_ID = "LK"
    INFO_POD_LINK_2_C2_ID_TABLE = "LL"
    POD_ENCODED_URL_1_LIVE_MARKETS = "LM"
    POD_ENCODED_URL_2 = "LN"
    DEFAULT_OPEN_LEFT = "LO"
    LIVE_IN_PLAY_INFO_POD_LINK_1_C3_ID = "LP"
    INFO_POD_LINK_1_C3_ID_TABLE = "LQ"
    INFO_POD_LINK_1_C3_SECTION_ID_LAST_RACES = "LR"
    PREVIOUS_SET_SCORE_SELECTED = "LS"
    MARKET = "MA"
    BET_CALL_V2_DISABLED_MAX_BET = "MB"
    CUSTOMER_TO_CUSTOMER_CALLING_FEATURE_DISABLED_COMMENT_V4_MARKET_COUNT = "MC"  # noqa: E501
    MATCHLIVE_PERIOD = "MD"
    MULTI_EVENT = "ME"
    MATCH_FLAG = "MF"
    MARKET_GROUP = "MG"
    MATCH_LENGTH = "ML"
    MERGE_MARKET = "MM"
    SECONDARY_UK_EVENT = "MO"
    MATCH_POSTPONED = "MP"
    CUSTOMER_TO_REPRESENTATIVE_CALLING_FEATURE_DISABLED_MORE_MARKETS = "MR"  # noqa: E501
    MEDIA_ID = "MS"
    BET_CALL_V2_TWILIO_DISABLED_MARKET_TYPE = "MT"
    MULTILINE = "MU"
    LOTTO_MAX_WINNINGS = "MW"
    MARKET_STYLE = "MY"
    NAME2 = "N2"
    NAME = "NA"
    CLOTH_NUMBER = "NC"
    NGENERA = "NG"
    NEXT_HEADER = "NH"
    NON_MATCH_BASED = "NM"
    NON_RUNNER = "NR"
    NEUTRAL_VENUE_TEXT = "NT"
    NEUTRAL_VENUE = "NV"
    BANKER_OPTION_OPEN_BETS_ENABLED = "OB"
    ODDS = "OD"
    ODDS_HISTORY = "OH"
    ODDS_OVERRIDE = "OO"
    OPEN_BETS_PRESENTATION_PULL_DISABLED_OPEN_BETS = "OP"
    ORDER = "OR"
    OTHERS_AVAILABLE = "OT"
    PARTICIPANT = "PA"
    PUSH_BALANCE_ENABLED = "PB"
    PAGE_DATA_1_PARTICIPANT_COUNT_PARTIAL_CASHOUT_AVAILABLE = "PC"
    PAGE_DATA_POD_INFO_POD_TYPE_PULL_DELAY = "PD"
    PARTICIPANTS_EXCEEDED_PERIOD = "PE"
    PUSH_FLAG = "PF"
    PENALTY_GOALS_MATCHLIVE_ADDITIONAL_INFO_PAGE_TYPE = "PG"
    PHONE_ONLY = "PH"
    PLAYING_INDICATOR_AUS_TOTE_COMBINATION = "PI"
    CLOTH_NUMBER_PULL = "PN"
    POD_STACK_ORDER_POINTS = "PO"
    POD_OPEN = "PP"
    PREFERENCE_ID_MARKET_GROUP_USER_PREFERENCE = "PR"
    POD_STACK_PARTICIPANT_STATUS = "PS"
    PRODUCT_TYPE_POD_TYPE = "PT"
    PREMIUM_VERSION = "PV"
    NO_OFFER = "PX"
    PARTICIPANT_STYLE = "PY"
    RANGE = "RA"
    RESULT_CODE = "RC"
    RACE_DETAILS = "RD"
    BET_RETURNS = "RE"
    REGION = "RG"
    R4_COMMENT = "RI"
    DEFAULT_OPEN_RIGHT_RACE_OFF = "RO"
    RUNNER_STATUS_REGULAR_SINGLE = "RS"
    RESULTS_TEXT = "RT"
    MATCHLIVE_STATS_1 = "S1"
    MATCHLIVE_STATS_2 = "S2"
    MATCHLIVE_STATS_3 = "S3"
    MATCHLIVE_STATS_4 = "S4"
    MATCHLIVE_STATS_5 = "S5"
    MATCHLIVE_STATS_6 = "S6"
    MATCHLIVE_STATS_7 = "S7"
    MATCHLIVE_STATS_8 = "S8"
    CHANGE_STAMP_SUSPEND_ARRAY = "SA"
    SCOREBOARD_TYPE = "SB"
    SCORE_SCORES_COLUMN = "SC"
    AUDIO_ID = "SD"
    SECONDARY_EVENT = "SE"
    SPOTLIGHT_FORM = "SF"
    STAT_GROUP = "SG"
    IMAGE_ID_PULL_SECTION_ID = "SI"
    SCORES_CELL = "SL"
    START_TIME = "SM"
    DRAW_NUMBER_PULL = "SN"
    STAT_PERIOD = "SP"
    SHORT_SCORE_SUSPENDED_SELECTION = "SS"
    INFO_POD_DETAIL_1_STAT_POD_BODY_TEXT_1_STAKE = "ST"
    SUCCESS_SUSPENDED = "SU"
    MATCHLIVE_AVAILABLE = "SV"
    STYLE = "SY"
    STAT_LOCATION = "SZ"
    C1_TABLE_MINI_DIARY_T1_TEXT_1 = "T1"
    C2_TABLE_MINI_DIARY_T2_TEXT_2 = "T2"
    MINI_DIARY_T3_TEXT_3 = "T3"
    TEXT_4 = "T4"
    TEXT_5 = "T5"
    TIME_ADDED = "TA"
    BREADCRUMB_TRAIL = "TB"
    BET_TOTE_TYPE_TEAM_COLOR = "TC"
    COUNTDOWN_TAX_DETAILS = "TD"
    TEAM = "TE"
    TEAM_GROUP = "TG"
    TMR_SERVER = "TI"
    LEAGUE_TOPIC_TOPIC_LIST = "TL"
    STAT_TIME_TMR_MINS = "TM"
    TRAINER_NAME = "TN"
    EMPTY_TOPIC_ID_PHONE_ONLY_LIST = "TO"
    TIME_STAMP = "TP"
    TAX_RATE_TOPIC_REFERENCE = "TR"
    TMR_SECS_TOTE_NAMES = "TS"
    TMR_TICKING = "TT"
    TMR_UPDATED = "TU"
    TAX_METHOD_TOPIC_LIST_EXCLUSIONS = "TX"
    CURRENT_INFO_V4 = "UC"
    UPDATE_FREQUENCY = "UF"
    VALUE = "VA"
    MATCHLIVE_ANIMATION = "VC"
    VIRTUAL_DATA = "VD"
    VIDEO_AVAILABLE = "VI"
    VISIBLE = "VL"
    VIRTUAL_RACE = "VR"
    VIDEO_STREAM = "VS"
    WIZE_GUY = "WG"
    WINNING_MARGIN = "WM"
    CHECK_BOX = "XB"
    EXCLUDE_COLUMN_NUMBERS = "XC"
    EXTRA_INFO_NODE_TEAM_MATCHTOTAL_QUOTE = "XI"
    CONTROLLER = "XL"
    SHORT_POINTS = "XP"
    EXTRA_TIME_LENGTH = "XT"
    MATCHLIVE_COORDINATES = "XY"
    TIMEZONE_ADJUSTMENT = "ZA"
    PADDOCK_VIDEO_AVAILABLE = "_V"


RESPONSE_OBJECT_FACTORY = {
    "result": "ResultResponse",
    "inplay_filter": "InPlayFilterResponse",
    "event": "InPlayOddsResponse",
    "prematch": "PreMatchOddsResponse",
    "inplay": "InPlayEventsResponse",
    "upcoming": "UpcomingEventsResponse",
}
