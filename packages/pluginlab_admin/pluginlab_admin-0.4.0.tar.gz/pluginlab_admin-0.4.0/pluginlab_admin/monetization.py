from dataclasses import dataclass
from typing import TypedDict
import requests

class _RawMemberQuotaUsageResponse(TypedDict):
    interval: str
    isOverLimit: bool
    isUnlimited: bool
    resetInDays: int
    usageCount: int
    usageLimit: int

@dataclass
class MemberQuotaUsage():
    interval: str
    is_overlimit: bool
    is_unlimited: bool
    reset_in_days: int
    usage_count: int
    usage_limit: int

class AppMonetization():
    """
    Access PluginLab's monetization-related features.
    """
    def __init__(self, plugin_id: str, secret: str, monetization_url: str) -> None:
        s = requests.Session()
        self.monetization_url = monetization_url
        s.headers.update({
            'X-PluginLab-Admin-Sdk-Secret': secret,
            'X-PluginLab-Plugin-Id': plugin_id
        })
        self.client = s

    def _make_api_url(self, path: str):
        return f'{self.monetization_url}{path}'

    def get_member_quota_usage(self, member_id: str) -> MemberQuotaUsage:
        """Get the quota usage of a given plugin member.
        Raises if the member is not found.
        """
        url = self._make_api_url(f'/admin/members/{member_id}/quota-usage')
        res = self.client.get(url)

        if not res.ok:
            raise Exception(res.text)

        raw_data: _RawMemberQuotaUsageResponse = res.json()

        return MemberQuotaUsage(
            interval=raw_data['interval'],
            is_overlimit=raw_data['isOverLimit'],
            is_unlimited=raw_data['isUnlimited'],
            reset_in_days=raw_data['resetInDays'],
            usage_count=raw_data['usageCount'],
            usage_limit=raw_data['usageLimit']
        )
