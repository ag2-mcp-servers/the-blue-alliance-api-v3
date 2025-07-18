# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T10:28:04+00:00



import argparse
import json
import os
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity
from fastapi import Header

from models import (
    APIStatus,
    DistrictDistrictKeyEventsGetResponse,
    DistrictDistrictKeyEventsKeysGetResponse,
    DistrictDistrictKeyEventsSimpleGetResponse,
    DistrictDistrictKeyRankingsGetResponse,
    DistrictDistrictKeyTeamsGetResponse,
    DistrictDistrictKeyTeamsKeysGetResponse,
    DistrictDistrictKeyTeamsSimpleGetResponse,
    DistrictsYearGetResponse,
    Event,
    EventDistrictPoints,
    EventEventKeyAlliancesGetResponse,
    EventEventKeyAwardsGetResponse,
    EventEventKeyMatchesGetResponse,
    EventEventKeyMatchesKeysGetResponse,
    EventEventKeyMatchesSimpleGetResponse,
    EventEventKeyMatchesTimeseriesGetResponse,
    EventEventKeyTeamsGetResponse,
    EventEventKeyTeamsKeysGetResponse,
    EventEventKeyTeamsSimpleGetResponse,
    EventEventKeyTeamsStatusesGetResponse,
    EventInsights,
    EventOPRs,
    EventPredictions,
    EventRanking,
    EventSimple,
    EventsYearGetResponse,
    EventsYearKeysGetResponse,
    EventsYearSimpleGetResponse,
    Match,
    MatchMatchKeyTimeseriesGetResponse,
    MatchSimple,
    Team,
    TeamEventStatus,
    TeamSimple,
    TeamsPageNumGetResponse,
    TeamsPageNumKeysGetResponse,
    TeamsPageNumSimpleGetResponse,
    TeamsYearPageNumGetResponse,
    TeamsYearPageNumKeysGetResponse,
    TeamsYearPageNumSimpleGetResponse,
    TeamTeamKeyAwardsGetResponse,
    TeamTeamKeyAwardsYearGetResponse,
    TeamTeamKeyDistrictsGetResponse,
    TeamTeamKeyEventEventKeyAwardsGetResponse,
    TeamTeamKeyEventEventKeyMatchesGetResponse,
    TeamTeamKeyEventEventKeyMatchesKeysGetResponse,
    TeamTeamKeyEventEventKeyMatchesSimpleGetResponse,
    TeamTeamKeyEventsGetResponse,
    TeamTeamKeyEventsKeysGetResponse,
    TeamTeamKeyEventsSimpleGetResponse,
    TeamTeamKeyEventsYearGetResponse,
    TeamTeamKeyEventsYearKeysGetResponse,
    TeamTeamKeyEventsYearSimpleGetResponse,
    TeamTeamKeyEventsYearStatusesGetResponse,
    TeamTeamKeyMatchesYearGetResponse,
    TeamTeamKeyMatchesYearKeysGetResponse,
    TeamTeamKeyMatchesYearSimpleGetResponse,
    TeamTeamKeyMediaTagMediaTagGetResponse,
    TeamTeamKeyMediaTagMediaTagYearGetResponse,
    TeamTeamKeyMediaYearGetResponse,
    TeamTeamKeyRobotsGetResponse,
    TeamTeamKeySocialMediaGetResponse,
    TeamTeamKeyYearsParticipatedGetResponse,
    Zebra,
)

app = MCPProxy(
    description='# Overview \n\n Information and statistics about FIRST Robotics Competition teams and events. \n\n# Authentication \n\nAll endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).',
    title='The Blue Alliance API v3',
    version='3.8.2',
    servers=[{'url': 'https://www.thebluealliance.com/api/v3'}],
)


@app.get(
    '/district/{district_key}/events',
    description=""" Gets a list of events in the given district. """,
    tags=[
        'district_management',
        'event_data_handling',
        'match_info_retrieval',
        'match_status_retrieval',
        'team_info_retrieval',
        'team_event_data_handling',
    ],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_district_events(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    district_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/district/{district_key}/events/keys',
    description=""" Gets a list of event keys for events in the given district. """,
    tags=['district_management', 'event_data_handling', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_district_events_keys(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    district_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/district/{district_key}/events/simple',
    description=""" Gets a short-form list of events in the given district. """,
    tags=[
        'district_management',
        'event_data_handling',
        'match_info_retrieval',
        'annual_event_processing',
        'match_status_retrieval',
        'team_info_retrieval',
        'team_event_data_handling',
        'team_year_based_data',
    ],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_district_events_simple(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    district_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/district/{district_key}/rankings',
    description=""" Gets a list of team district rankings for the given district. """,
    tags=['district_management'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_district_rankings(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    district_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/district/{district_key}/teams',
    description=""" Gets a list of `Team` objects that competed in events in the given district. """,
    tags=['district_management', 'event_data_handling', 'match_info_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_district_teams(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    district_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/district/{district_key}/teams/keys',
    description=""" Gets a list of `Team` objects that competed in events in the given district. """,
    tags=['district_management'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_district_teams_keys(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    district_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/district/{district_key}/teams/simple',
    description=""" Gets a short-form list of `Team` objects that competed in events in the given district. """,
    tags=['district_management'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_district_teams_simple(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    district_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/districts/{year}',
    description=""" Gets a list of districts and their corresponding district key, for the given year. """,
    tags=['annual_event_processing'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_districts_by_year(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    year: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/event/{event_key}',
    description=""" Gets an Event. """,
    tags=['event_data_handling', 'match_info_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_event(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/event/{event_key}/alliances',
    description=""" Gets a list of Elimination Alliances for the given Event. """,
    tags=['event_data_handling', 'match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_event_alliances(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/event/{event_key}/awards',
    description=""" Gets a list of awards from the given event. """,
    tags=['event_data_handling', 'match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_event_awards(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/event/{event_key}/district_points',
    description=""" Gets a list of team rankings for the Event. """,
    tags=['event_data_handling', 'match_status_retrieval', 'team_event_data_handling'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_event_district_points(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/event/{event_key}/insights',
    description=""" Gets a set of Event-specific insights for the given Event. """,
    tags=['event_data_handling', 'match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_event_insights(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/event/{event_key}/matches',
    description=""" Gets a list of matches for the given event. """,
    tags=['event_data_handling', 'match_info_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_event_matches(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/event/{event_key}/matches/keys',
    description=""" Gets a list of match keys for the given event. """,
    tags=['event_data_handling', 'match_info_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_event_matches_keys(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/event/{event_key}/matches/simple',
    description=""" Gets a short-form list of matches for the given event. """,
    tags=['event_data_handling', 'match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_event_matches_simple(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/event/{event_key}/matches/timeseries',
    description=""" Gets an array of Match Keys for the given event key that have timeseries data. Returns an empty array if no matches have timeseries data.
*WARNING:* This is *not* official data, and is subject to a significant possibility of error, or missing data. Do not rely on this data for any purpose. In fact, pretend we made it up.
*WARNING:* This endpoint and corresponding data models are under *active development* and may change at any time, including in breaking ways. """,
    tags=['event_data_handling', 'match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_event_match_timeseries(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/event/{event_key}/oprs',
    description=""" Gets a set of Event OPRs (including OPR, DPR, and CCWM) for the given Event. """,
    tags=['event_data_handling', 'match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_event_o_p_rs(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/event/{event_key}/predictions',
    description=""" Gets information on TBA-generated predictions for the given Event. Contains year-specific information. *WARNING* This endpoint is currently under development and may change at any time. """,
    tags=['event_data_handling', 'match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_event_predictions(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/event/{event_key}/rankings',
    description=""" Gets a list of team rankings for the Event. """,
    tags=['event_data_handling', 'match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_event_rankings(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/event/{event_key}/simple',
    description=""" Gets a short-form Event. """,
    tags=['event_data_handling', 'match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_event_simple(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/event/{event_key}/teams',
    description=""" Gets a list of `Team` objects that competed in the given event. """,
    tags=['event_data_handling', 'match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_event_teams(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/event/{event_key}/teams/keys',
    description=""" Gets a list of `Team` keys that competed in the given event. """,
    tags=['event_data_handling', 'match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_event_teams_keys(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/event/{event_key}/teams/simple',
    description=""" Gets a short-form list of `Team` objects that competed in the given event. """,
    tags=['event_data_handling', 'match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_event_teams_simple(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/event/{event_key}/teams/statuses',
    description=""" Gets a key-value list of the event statuses for teams competing at the given event. """,
    tags=['event_data_handling', 'match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_event_teams_statuses(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/events/{year}',
    description=""" Gets a list of events in the given year. """,
    tags=['annual_event_processing', 'event_data_handling'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_events_by_year(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    year: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/events/{year}/keys',
    description=""" Gets a list of event keys in the given year. """,
    tags=['annual_event_processing', 'match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_events_by_year_keys(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    year: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/events/{year}/simple',
    description=""" Gets a short-form list of events in the given year. """,
    tags=['annual_event_processing'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_events_by_year_simple(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    year: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/match/{match_key}',
    description=""" Gets a `Match` object for the given match key. """,
    tags=['match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_match(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    match_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/match/{match_key}/simple',
    description=""" Gets a short-form `Match` object for the given match key. """,
    tags=['match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_match_simple(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    match_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/match/{match_key}/timeseries',
    description=""" Gets an array of game-specific Match Timeseries objects for the given match key or an empty array if not available.
*WARNING:* This is *not* official data, and is subject to a significant possibility of error, or missing data. Do not rely on this data for any purpose. In fact, pretend we made it up.
*WARNING:* This endpoint and corresponding data models are under *active development* and may change at any time, including in breaking ways. """,
    tags=['match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_match_timeseries(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    match_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/match/{match_key}/zebra_motionworks',
    description=""" Gets Zebra MotionWorks data for a Match for the given match key. """,
    tags=['match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_match_zebra(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    match_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/status',
    description=""" Returns API status, and TBA status information. """,
    tags=['match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_status(if__none__match: Optional[str] = Header(None, alias='If-None-Match')):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}',
    description=""" Gets a `Team` object for the team referenced by the given key. """,
    tags=['team_info_retrieval', 'team_event_data_handling'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/awards',
    description=""" Gets a list of awards the given team has won. """,
    tags=['team_info_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_awards(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/awards/{year}',
    description=""" Gets a list of awards the given team has won in a given year. """,
    tags=['team_year_based_data', 'annual_event_processing'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_awards_by_year(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
    year: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/districts',
    description=""" Gets an array of districts representing each year the team was in a district. Will return an empty array if the team was never in a district. """,
    tags=['team_info_retrieval', 'team_event_data_handling'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_districts(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/event/{event_key}/awards',
    description=""" Gets a list of awards the given team won at the given event. """,
    tags=[
        'district_management',
        'event_data_handling',
        'team_info_retrieval',
        'team_event_data_handling',
    ],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_event_awards(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/event/{event_key}/matches',
    description=""" Gets a list of matches for the given team and event. """,
    tags=['event_data_handling', 'match_info_retrieval', 'team_info_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_event_matches(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/event/{event_key}/matches/keys',
    description=""" Gets a list of match keys for matches for the given team and event. """,
    tags=['team_event_data_handling'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_event_matches_keys(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/event/{event_key}/matches/simple',
    description=""" Gets a short-form list of matches for the given team and event. """,
    tags=['team_event_data_handling', 'event_data_handling'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_event_matches_simple(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/event/{event_key}/status',
    description=""" Gets the competition rank and status of the team at the given event. """,
    tags=['team_event_data_handling', 'event_data_handling'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_event_status(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
    event_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/events',
    description=""" Gets a list of all events this team has competed at. """,
    tags=['district_management', 'team_info_retrieval', 'team_event_data_handling'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_events(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/events/keys',
    description=""" Gets a list of the event keys for all events this team has competed at. """,
    tags=['team_info_retrieval', 'team_event_data_handling'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_events_keys(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/events/simple',
    description=""" Gets a short-form list of all events this team has competed at. """,
    tags=['district_management', 'team_info_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_events_simple(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/events/{year}',
    description=""" Gets a list of events this team has competed at in the given year. """,
    tags=['team_year_based_data', 'team_info_retrieval', 'annual_event_processing'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_events_by_year(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
    year: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/events/{year}/keys',
    description=""" Gets a list of the event keys for events this team has competed at in the given year. """,
    tags=['team_year_based_data', 'annual_event_processing'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_events_by_year_keys(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
    year: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/events/{year}/simple',
    description=""" Gets a short-form list of events this team has competed at in the given year. """,
    tags=['team_year_based_data', 'team_info_retrieval', 'match_info_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_events_by_year_simple(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
    year: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/events/{year}/statuses',
    description=""" Gets a key-value list of the event statuses for events this team has competed at in the given year. """,
    tags=['team_year_based_data', 'event_data_handling', 'team_info_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_events_statuses_by_year(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
    year: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/matches/{year}',
    description=""" Gets a list of matches for the given team and year. """,
    tags=['annual_event_processing', 'team_year_based_data'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_matches_by_year(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
    year: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/matches/{year}/keys',
    description=""" Gets a list of match keys for matches for the given team and year. """,
    tags=['team_year_based_data', 'team_info_retrieval', 'annual_event_processing'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_matches_by_year_keys(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
    year: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/matches/{year}/simple',
    description=""" Gets a short-form list of matches for the given team and year. """,
    tags=['team_year_based_data', 'team_info_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_matches_by_year_simple(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
    year: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/media/tag/{media_tag}',
    description=""" Gets a list of Media (videos / pictures) for the given team and tag. """,
    tags=['team_event_data_handling', 'match_info_retrieval', 'team_info_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_media_by_tag(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
    media_tag: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/media/tag/{media_tag}/{year}',
    description=""" Gets a list of Media (videos / pictures) for the given team, tag and year. """,
    tags=['team_year_based_data', 'team_info_retrieval', 'event_data_handling'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_media_by_tag_year(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
    media_tag: str = ...,
    year: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/media/{year}',
    description=""" Gets a list of Media (videos / pictures) for the given team and year. """,
    tags=['team_year_based_data', 'team_info_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_media_by_year(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
    year: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/robots',
    description=""" Gets a list of year and robot name pairs for each year that a robot name was provided. Will return an empty array if the team has never named a robot. """,
    tags=['team_info_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_robots(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/simple',
    description=""" Gets a `Team_Simple` object for the team referenced by the given key. """,
    tags=['district_management', 'event_data_handling', 'match_info_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_simple(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/social_media',
    description=""" Gets a list of Media (social media) for the given team. """,
    tags=['team_info_retrieval', 'team_event_data_handling'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_social_media(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/team/{team_key}/years_participated',
    description=""" Gets a list of years in which the team participated in at least one competition. """,
    tags=['district_management', 'team_info_retrieval', 'team_event_data_handling'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_team_years_participated(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    team_key: str = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/teams/{page_num}',
    description=""" Gets a list of `Team` objects, paginated in groups of 500. """,
    tags=['match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_teams(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    page_num: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/teams/{page_num}/keys',
    description=""" Gets a list of Team keys, paginated in groups of 500. (Note, each page will not have 500 teams, but will include the teams within that range of 500.) """,
    tags=['match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_teams_keys(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    page_num: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/teams/{page_num}/simple',
    description=""" Gets a list of short form `Team_Simple` objects, paginated in groups of 500. """,
    tags=['match_info_retrieval', 'match_status_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_teams_simple(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    page_num: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/teams/{year}/{page_num}',
    description=""" Gets a list of `Team` objects that competed in the given year, paginated in groups of 500. """,
    tags=['annual_event_processing', 'match_info_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_teams_by_year(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    year: int = ...,
    page_num: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/teams/{year}/{page_num}/keys',
    description=""" Gets a list Team Keys that competed in the given year, paginated in groups of 500. """,
    tags=['annual_event_processing', 'match_info_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_teams_by_year_keys(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    year: int = ...,
    page_num: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/teams/{year}/{page_num}/simple',
    description=""" Gets a list of short form `Team_Simple` objects that competed in the given year, paginated in groups of 500. """,
    tags=['annual_event_processing', 'match_info_retrieval'],
    security=[
        APIKeyHeader(name="X-TBA-Auth-Key"),
    ],
)
def get_teams_by_year_simple(
    if__none__match: Optional[str] = Header(None, alias='If-None-Match'),
    year: int = ...,
    page_num: int = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
