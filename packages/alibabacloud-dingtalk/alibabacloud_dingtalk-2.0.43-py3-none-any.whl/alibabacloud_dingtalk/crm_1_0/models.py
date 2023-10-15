# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AbandonCustomerHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AbandonCustomerRequest(TeaModel):
    def __init__(
        self,
        custom_track_desc: str = None,
        instance_id_list: List[str] = None,
        operator_user_id: str = None,
        opt_type: str = None,
    ):
        self.custom_track_desc = custom_track_desc
        self.instance_id_list = instance_id_list
        self.operator_user_id = operator_user_id
        self.opt_type = opt_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_track_desc is not None:
            result['customTrackDesc'] = self.custom_track_desc
        if self.instance_id_list is not None:
            result['instanceIdList'] = self.instance_id_list
        if self.operator_user_id is not None:
            result['operatorUserId'] = self.operator_user_id
        if self.opt_type is not None:
            result['optType'] = self.opt_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customTrackDesc') is not None:
            self.custom_track_desc = m.get('customTrackDesc')
        if m.get('instanceIdList') is not None:
            self.instance_id_list = m.get('instanceIdList')
        if m.get('operatorUserId') is not None:
            self.operator_user_id = m.get('operatorUserId')
        if m.get('optType') is not None:
            self.opt_type = m.get('optType')
        return self


class AbandonCustomerResponseBody(TeaModel):
    def __init__(
        self,
        instance_id_list: List[str] = None,
    ):
        self.instance_id_list = instance_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id_list is not None:
            result['instanceIdList'] = self.instance_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceIdList') is not None:
            self.instance_id_list = m.get('instanceIdList')
        return self


class AbandonCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AbandonCustomerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AbandonCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddCrmPersonalCustomerHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AddCrmPersonalCustomerRequestPermission(TeaModel):
    def __init__(
        self,
        owner_staff_ids: List[str] = None,
        participant_staff_ids: List[str] = None,
    ):
        self.owner_staff_ids = owner_staff_ids
        self.participant_staff_ids = participant_staff_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_staff_ids is not None:
            result['ownerStaffIds'] = self.owner_staff_ids
        if self.participant_staff_ids is not None:
            result['participantStaffIds'] = self.participant_staff_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ownerStaffIds') is not None:
            self.owner_staff_ids = m.get('ownerStaffIds')
        if m.get('participantStaffIds') is not None:
            self.participant_staff_ids = m.get('participantStaffIds')
        return self


class AddCrmPersonalCustomerRequest(TeaModel):
    def __init__(
        self,
        action: str = None,
        creator_nick: str = None,
        creator_user_id: str = None,
        data: Dict[str, Any] = None,
        extend_data: Dict[str, Any] = None,
        permission: AddCrmPersonalCustomerRequestPermission = None,
        relation_type: str = None,
        skip_duplicate_check: bool = None,
    ):
        self.action = action
        self.creator_nick = creator_nick
        self.creator_user_id = creator_user_id
        self.data = data
        self.extend_data = extend_data
        self.permission = permission
        self.relation_type = relation_type
        self.skip_duplicate_check = skip_duplicate_check

    def validate(self):
        if self.permission:
            self.permission.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.creator_nick is not None:
            result['creatorNick'] = self.creator_nick
        if self.creator_user_id is not None:
            result['creatorUserId'] = self.creator_user_id
        if self.data is not None:
            result['data'] = self.data
        if self.extend_data is not None:
            result['extendData'] = self.extend_data
        if self.permission is not None:
            result['permission'] = self.permission.to_map()
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        if self.skip_duplicate_check is not None:
            result['skipDuplicateCheck'] = self.skip_duplicate_check
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('creatorNick') is not None:
            self.creator_nick = m.get('creatorNick')
        if m.get('creatorUserId') is not None:
            self.creator_user_id = m.get('creatorUserId')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('extendData') is not None:
            self.extend_data = m.get('extendData')
        if m.get('permission') is not None:
            temp_model = AddCrmPersonalCustomerRequestPermission()
            self.permission = temp_model.from_map(m['permission'])
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        if m.get('skipDuplicateCheck') is not None:
            self.skip_duplicate_check = m.get('skipDuplicateCheck')
        return self


class AddCrmPersonalCustomerResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class AddCrmPersonalCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddCrmPersonalCustomerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddCrmPersonalCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddCustomerTrackHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AddCustomerTrackRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        customer_id: str = None,
        extra_biz_info: str = None,
        idempotent_key: str = None,
        masked_content: str = None,
        operator_user_id: str = None,
        relation_type: str = None,
        title: str = None,
        type: int = None,
    ):
        self.content = content
        self.customer_id = customer_id
        self.extra_biz_info = extra_biz_info
        self.idempotent_key = idempotent_key
        self.masked_content = masked_content
        self.operator_user_id = operator_user_id
        self.relation_type = relation_type
        self.title = title
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.extra_biz_info is not None:
            result['extraBizInfo'] = self.extra_biz_info
        if self.idempotent_key is not None:
            result['idempotentKey'] = self.idempotent_key
        if self.masked_content is not None:
            result['maskedContent'] = self.masked_content
        if self.operator_user_id is not None:
            result['operatorUserId'] = self.operator_user_id
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        if self.title is not None:
            result['title'] = self.title
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('extraBizInfo') is not None:
            self.extra_biz_info = m.get('extraBizInfo')
        if m.get('idempotentKey') is not None:
            self.idempotent_key = m.get('idempotentKey')
        if m.get('maskedContent') is not None:
            self.masked_content = m.get('maskedContent')
        if m.get('operatorUserId') is not None:
            self.operator_user_id = m.get('operatorUserId')
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AddCustomerTrackResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AddCustomerTrackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddCustomerTrackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddCustomerTrackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddLeadsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AddLeadsRequestLeads(TeaModel):
    def __init__(
        self,
        leads_name: str = None,
        out_leads_id: str = None,
    ):
        self.leads_name = leads_name
        self.out_leads_id = out_leads_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.leads_name is not None:
            result['leadsName'] = self.leads_name
        if self.out_leads_id is not None:
            result['outLeadsId'] = self.out_leads_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('leadsName') is not None:
            self.leads_name = m.get('leadsName')
        if m.get('outLeadsId') is not None:
            self.out_leads_id = m.get('outLeadsId')
        return self


class AddLeadsRequest(TeaModel):
    def __init__(
        self,
        assign_timestamp: int = None,
        assign_user_id: str = None,
        assigned_user_id: str = None,
        leads: List[AddLeadsRequestLeads] = None,
        out_task_id: str = None,
    ):
        self.assign_timestamp = assign_timestamp
        self.assign_user_id = assign_user_id
        self.assigned_user_id = assigned_user_id
        self.leads = leads
        self.out_task_id = out_task_id

    def validate(self):
        if self.leads:
            for k in self.leads:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_timestamp is not None:
            result['assignTimestamp'] = self.assign_timestamp
        if self.assign_user_id is not None:
            result['assignUserId'] = self.assign_user_id
        if self.assigned_user_id is not None:
            result['assignedUserId'] = self.assigned_user_id
        result['leads'] = []
        if self.leads is not None:
            for k in self.leads:
                result['leads'].append(k.to_map() if k else None)
        if self.out_task_id is not None:
            result['outTaskId'] = self.out_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assignTimestamp') is not None:
            self.assign_timestamp = m.get('assignTimestamp')
        if m.get('assignUserId') is not None:
            self.assign_user_id = m.get('assignUserId')
        if m.get('assignedUserId') is not None:
            self.assigned_user_id = m.get('assignedUserId')
        self.leads = []
        if m.get('leads') is not None:
            for k in m.get('leads'):
                temp_model = AddLeadsRequestLeads()
                self.leads.append(temp_model.from_map(k))
        if m.get('outTaskId') is not None:
            self.out_task_id = m.get('outTaskId')
        return self


class AddLeadsResponseBody(TeaModel):
    def __init__(
        self,
        out_task_id: str = None,
    ):
        self.out_task_id = out_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_task_id is not None:
            result['outTaskId'] = self.out_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('outTaskId') is not None:
            self.out_task_id = m.get('outTaskId')
        return self


class AddLeadsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddLeadsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddLeadsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRelationMetaFieldHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AddRelationMetaFieldRequestFieldDTOListPropsOptions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class AddRelationMetaFieldRequestFieldDTOListProps(TeaModel):
    def __init__(
        self,
        align: str = None,
        biz_alias: str = None,
        choice: int = None,
        content: str = None,
        disabled: bool = None,
        duration: bool = None,
        field_id: str = None,
        format: str = None,
        invisible: bool = None,
        label: str = None,
        label_editable_freeze: bool = None,
        link: str = None,
        need_detail: str = None,
        not_print: str = None,
        not_upper: str = None,
        options: List[AddRelationMetaFieldRequestFieldDTOListPropsOptions] = None,
        pay_enable: bool = None,
        placeholder: str = None,
        required: bool = None,
        required_editable_freeze: bool = None,
        sortable: bool = None,
        unit: str = None,
    ):
        self.align = align
        self.biz_alias = biz_alias
        self.choice = choice
        self.content = content
        self.disabled = disabled
        self.duration = duration
        self.field_id = field_id
        self.format = format
        self.invisible = invisible
        self.label = label
        self.label_editable_freeze = label_editable_freeze
        self.link = link
        self.need_detail = need_detail
        self.not_print = not_print
        self.not_upper = not_upper
        self.options = options
        self.pay_enable = pay_enable
        self.placeholder = placeholder
        self.required = required
        self.required_editable_freeze = required_editable_freeze
        self.sortable = sortable
        self.unit = unit

    def validate(self):
        if self.options:
            for k in self.options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align is not None:
            result['align'] = self.align
        if self.biz_alias is not None:
            result['bizAlias'] = self.biz_alias
        if self.choice is not None:
            result['choice'] = self.choice
        if self.content is not None:
            result['content'] = self.content
        if self.disabled is not None:
            result['disabled'] = self.disabled
        if self.duration is not None:
            result['duration'] = self.duration
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.format is not None:
            result['format'] = self.format
        if self.invisible is not None:
            result['invisible'] = self.invisible
        if self.label is not None:
            result['label'] = self.label
        if self.label_editable_freeze is not None:
            result['labelEditableFreeze'] = self.label_editable_freeze
        if self.link is not None:
            result['link'] = self.link
        if self.need_detail is not None:
            result['needDetail'] = self.need_detail
        if self.not_print is not None:
            result['notPrint'] = self.not_print
        if self.not_upper is not None:
            result['notUpper'] = self.not_upper
        result['options'] = []
        if self.options is not None:
            for k in self.options:
                result['options'].append(k.to_map() if k else None)
        if self.pay_enable is not None:
            result['payEnable'] = self.pay_enable
        if self.placeholder is not None:
            result['placeholder'] = self.placeholder
        if self.required is not None:
            result['required'] = self.required
        if self.required_editable_freeze is not None:
            result['requiredEditableFreeze'] = self.required_editable_freeze
        if self.sortable is not None:
            result['sortable'] = self.sortable
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('align') is not None:
            self.align = m.get('align')
        if m.get('bizAlias') is not None:
            self.biz_alias = m.get('bizAlias')
        if m.get('choice') is not None:
            self.choice = m.get('choice')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('invisible') is not None:
            self.invisible = m.get('invisible')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('labelEditableFreeze') is not None:
            self.label_editable_freeze = m.get('labelEditableFreeze')
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('needDetail') is not None:
            self.need_detail = m.get('needDetail')
        if m.get('notPrint') is not None:
            self.not_print = m.get('notPrint')
        if m.get('notUpper') is not None:
            self.not_upper = m.get('notUpper')
        self.options = []
        if m.get('options') is not None:
            for k in m.get('options'):
                temp_model = AddRelationMetaFieldRequestFieldDTOListPropsOptions()
                self.options.append(temp_model.from_map(k))
        if m.get('payEnable') is not None:
            self.pay_enable = m.get('payEnable')
        if m.get('placeholder') is not None:
            self.placeholder = m.get('placeholder')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('requiredEditableFreeze') is not None:
            self.required_editable_freeze = m.get('requiredEditableFreeze')
        if m.get('sortable') is not None:
            self.sortable = m.get('sortable')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class AddRelationMetaFieldRequestFieldDTOList(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        props: AddRelationMetaFieldRequestFieldDTOListProps = None,
    ):
        self.component_name = component_name
        self.props = props

    def validate(self):
        if self.props:
            self.props.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.props is not None:
            result['props'] = self.props.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('props') is not None:
            temp_model = AddRelationMetaFieldRequestFieldDTOListProps()
            self.props = temp_model.from_map(m['props'])
        return self


class AddRelationMetaFieldRequest(TeaModel):
    def __init__(
        self,
        field_dtolist: List[AddRelationMetaFieldRequestFieldDTOList] = None,
        operator_user_id: str = None,
        relation_type: str = None,
        tenant: str = None,
    ):
        self.field_dtolist = field_dtolist
        self.operator_user_id = operator_user_id
        self.relation_type = relation_type
        self.tenant = tenant

    def validate(self):
        if self.field_dtolist:
            for k in self.field_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['fieldDTOList'] = []
        if self.field_dtolist is not None:
            for k in self.field_dtolist:
                result['fieldDTOList'].append(k.to_map() if k else None)
        if self.operator_user_id is not None:
            result['operatorUserId'] = self.operator_user_id
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        if self.tenant is not None:
            result['tenant'] = self.tenant
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.field_dtolist = []
        if m.get('fieldDTOList') is not None:
            for k in m.get('fieldDTOList'):
                temp_model = AddRelationMetaFieldRequestFieldDTOList()
                self.field_dtolist.append(temp_model.from_map(k))
        if m.get('operatorUserId') is not None:
            self.operator_user_id = m.get('operatorUserId')
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        if m.get('tenant') is not None:
            self.tenant = m.get('tenant')
        return self


class AddRelationMetaFieldResponseBody(TeaModel):
    def __init__(
        self,
        relation_type: str = None,
    ):
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        return self


class AddRelationMetaFieldResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddRelationMetaFieldResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddRelationMetaFieldResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddContactsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class BatchAddContactsRequestRelationListBizDataList(TeaModel):
    def __init__(
        self,
        extend_value: str = None,
        key: str = None,
        value: str = None,
    ):
        self.extend_value = extend_value
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_value is not None:
            result['extendValue'] = self.extend_value
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extendValue') is not None:
            self.extend_value = m.get('extendValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class BatchAddContactsRequestRelationList(TeaModel):
    def __init__(
        self,
        biz_data_list: List[BatchAddContactsRequestRelationListBizDataList] = None,
        biz_ext_map: Dict[str, str] = None,
    ):
        self.biz_data_list = biz_data_list
        self.biz_ext_map = biz_ext_map

    def validate(self):
        if self.biz_data_list:
            for k in self.biz_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['bizDataList'] = []
        if self.biz_data_list is not None:
            for k in self.biz_data_list:
                result['bizDataList'].append(k.to_map() if k else None)
        if self.biz_ext_map is not None:
            result['bizExtMap'] = self.biz_ext_map
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_data_list = []
        if m.get('bizDataList') is not None:
            for k in m.get('bizDataList'):
                temp_model = BatchAddContactsRequestRelationListBizDataList()
                self.biz_data_list.append(temp_model.from_map(k))
        if m.get('bizExtMap') is not None:
            self.biz_ext_map = m.get('bizExtMap')
        return self


class BatchAddContactsRequest(TeaModel):
    def __init__(
        self,
        operator_user_id: str = None,
        relation_list: List[BatchAddContactsRequestRelationList] = None,
    ):
        self.operator_user_id = operator_user_id
        self.relation_list = relation_list

    def validate(self):
        if self.relation_list:
            for k in self.relation_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_user_id is not None:
            result['operatorUserId'] = self.operator_user_id
        result['relationList'] = []
        if self.relation_list is not None:
            for k in self.relation_list:
                result['relationList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operatorUserId') is not None:
            self.operator_user_id = m.get('operatorUserId')
        self.relation_list = []
        if m.get('relationList') is not None:
            for k in m.get('relationList'):
                temp_model = BatchAddContactsRequestRelationList()
                self.relation_list.append(temp_model.from_map(k))
        return self


class BatchAddContactsResponseBodyResults(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        relation_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.relation_id = relation_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.relation_id is not None:
            result['relationId'] = self.relation_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('relationId') is not None:
            self.relation_id = m.get('relationId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BatchAddContactsResponseBody(TeaModel):
    def __init__(
        self,
        results: List[BatchAddContactsResponseBodyResults] = None,
    ):
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = BatchAddContactsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchAddContactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchAddContactsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchAddContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddFollowRecordsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class BatchAddFollowRecordsRequestInstanceListDataArray(TeaModel):
    def __init__(
        self,
        extend_value: str = None,
        key: str = None,
        value: str = None,
    ):
        self.extend_value = extend_value
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_value is not None:
            result['extendValue'] = self.extend_value
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extendValue') is not None:
            self.extend_value = m.get('extendValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class BatchAddFollowRecordsRequestInstanceList(TeaModel):
    def __init__(
        self,
        data_array: List[BatchAddFollowRecordsRequestInstanceListDataArray] = None,
    ):
        self.data_array = data_array

    def validate(self):
        if self.data_array:
            for k in self.data_array:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dataArray'] = []
        if self.data_array is not None:
            for k in self.data_array:
                result['dataArray'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_array = []
        if m.get('dataArray') is not None:
            for k in m.get('dataArray'):
                temp_model = BatchAddFollowRecordsRequestInstanceListDataArray()
                self.data_array.append(temp_model.from_map(k))
        return self


class BatchAddFollowRecordsRequest(TeaModel):
    def __init__(
        self,
        instance_list: List[BatchAddFollowRecordsRequestInstanceList] = None,
        operator_user_id: str = None,
    ):
        self.instance_list = instance_list
        self.operator_user_id = operator_user_id

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['instanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['instanceList'].append(k.to_map() if k else None)
        if self.operator_user_id is not None:
            result['operatorUserId'] = self.operator_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_list = []
        if m.get('instanceList') is not None:
            for k in m.get('instanceList'):
                temp_model = BatchAddFollowRecordsRequestInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        if m.get('operatorUserId') is not None:
            self.operator_user_id = m.get('operatorUserId')
        return self


class BatchAddFollowRecordsResponseBodyResults(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        instance_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.instance_id = instance_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BatchAddFollowRecordsResponseBody(TeaModel):
    def __init__(
        self,
        results: List[BatchAddFollowRecordsResponseBodyResults] = None,
    ):
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = BatchAddFollowRecordsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchAddFollowRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchAddFollowRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchAddFollowRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddRelationDatasHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class BatchAddRelationDatasRequestRelationListBizDataList(TeaModel):
    def __init__(
        self,
        extend_value: str = None,
        key: str = None,
        value: str = None,
    ):
        self.extend_value = extend_value
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_value is not None:
            result['extendValue'] = self.extend_value
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extendValue') is not None:
            self.extend_value = m.get('extendValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class BatchAddRelationDatasRequestRelationListRelationPermissionDTO(TeaModel):
    def __init__(
        self,
        participant_user_ids: List[str] = None,
        principal_user_ids: List[str] = None,
    ):
        self.participant_user_ids = participant_user_ids
        self.principal_user_ids = principal_user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.participant_user_ids is not None:
            result['participantUserIds'] = self.participant_user_ids
        if self.principal_user_ids is not None:
            result['principalUserIds'] = self.principal_user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('participantUserIds') is not None:
            self.participant_user_ids = m.get('participantUserIds')
        if m.get('principalUserIds') is not None:
            self.principal_user_ids = m.get('principalUserIds')
        return self


class BatchAddRelationDatasRequestRelationList(TeaModel):
    def __init__(
        self,
        biz_data_list: List[BatchAddRelationDatasRequestRelationListBizDataList] = None,
        biz_ext_map: Dict[str, str] = None,
        relation_permission_dto: BatchAddRelationDatasRequestRelationListRelationPermissionDTO = None,
    ):
        self.biz_data_list = biz_data_list
        self.biz_ext_map = biz_ext_map
        self.relation_permission_dto = relation_permission_dto

    def validate(self):
        if self.biz_data_list:
            for k in self.biz_data_list:
                if k:
                    k.validate()
        if self.relation_permission_dto:
            self.relation_permission_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['bizDataList'] = []
        if self.biz_data_list is not None:
            for k in self.biz_data_list:
                result['bizDataList'].append(k.to_map() if k else None)
        if self.biz_ext_map is not None:
            result['bizExtMap'] = self.biz_ext_map
        if self.relation_permission_dto is not None:
            result['relationPermissionDTO'] = self.relation_permission_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_data_list = []
        if m.get('bizDataList') is not None:
            for k in m.get('bizDataList'):
                temp_model = BatchAddRelationDatasRequestRelationListBizDataList()
                self.biz_data_list.append(temp_model.from_map(k))
        if m.get('bizExtMap') is not None:
            self.biz_ext_map = m.get('bizExtMap')
        if m.get('relationPermissionDTO') is not None:
            temp_model = BatchAddRelationDatasRequestRelationListRelationPermissionDTO()
            self.relation_permission_dto = temp_model.from_map(m['relationPermissionDTO'])
        return self


class BatchAddRelationDatasRequest(TeaModel):
    def __init__(
        self,
        operator_user_id: str = None,
        relation_list: List[BatchAddRelationDatasRequestRelationList] = None,
        relation_type: str = None,
        skip_duplicate_check: bool = None,
    ):
        self.operator_user_id = operator_user_id
        self.relation_list = relation_list
        self.relation_type = relation_type
        self.skip_duplicate_check = skip_duplicate_check

    def validate(self):
        if self.relation_list:
            for k in self.relation_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_user_id is not None:
            result['operatorUserId'] = self.operator_user_id
        result['relationList'] = []
        if self.relation_list is not None:
            for k in self.relation_list:
                result['relationList'].append(k.to_map() if k else None)
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        if self.skip_duplicate_check is not None:
            result['skipDuplicateCheck'] = self.skip_duplicate_check
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operatorUserId') is not None:
            self.operator_user_id = m.get('operatorUserId')
        self.relation_list = []
        if m.get('relationList') is not None:
            for k in m.get('relationList'):
                temp_model = BatchAddRelationDatasRequestRelationList()
                self.relation_list.append(temp_model.from_map(k))
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        if m.get('skipDuplicateCheck') is not None:
            self.skip_duplicate_check = m.get('skipDuplicateCheck')
        return self


class BatchAddRelationDatasResponseBodyResults(TeaModel):
    def __init__(
        self,
        duplicated_relation_ids: List[str] = None,
        error_code: str = None,
        error_msg: str = None,
        relation_id: str = None,
        success: bool = None,
    ):
        self.duplicated_relation_ids = duplicated_relation_ids
        self.error_code = error_code
        self.error_msg = error_msg
        self.relation_id = relation_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duplicated_relation_ids is not None:
            result['duplicatedRelationIds'] = self.duplicated_relation_ids
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.relation_id is not None:
            result['relationId'] = self.relation_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duplicatedRelationIds') is not None:
            self.duplicated_relation_ids = m.get('duplicatedRelationIds')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('relationId') is not None:
            self.relation_id = m.get('relationId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BatchAddRelationDatasResponseBody(TeaModel):
    def __init__(
        self,
        results: List[BatchAddRelationDatasResponseBodyResults] = None,
    ):
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = BatchAddRelationDatasResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchAddRelationDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchAddRelationDatasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchAddRelationDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchRemoveFollowRecordsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class BatchRemoveFollowRecordsRequest(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        operator_user_id: str = None,
    ):
        self.instance_ids = instance_ids
        self.operator_user_id = operator_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.operator_user_id is not None:
            result['operatorUserId'] = self.operator_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('operatorUserId') is not None:
            self.operator_user_id = m.get('operatorUserId')
        return self


class BatchRemoveFollowRecordsResponseBodyResults(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        instance_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.instance_id = instance_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BatchRemoveFollowRecordsResponseBody(TeaModel):
    def __init__(
        self,
        results: List[BatchRemoveFollowRecordsResponseBodyResults] = None,
    ):
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = BatchRemoveFollowRecordsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchRemoveFollowRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchRemoveFollowRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchRemoveFollowRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSendOfficialAccountOTOMessageHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList(TeaModel):
    def __init__(
        self,
        action_url: str = None,
        title: str = None,
    ):
        self.action_url = action_url
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_url is not None:
            result['actionUrl'] = self.action_url
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionUrl') is not None:
            self.action_url = m.get('actionUrl')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard(TeaModel):
    def __init__(
        self,
        button_list: List[BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList] = None,
        button_orientation: str = None,
        markdown: str = None,
        single_title: str = None,
        single_url: str = None,
        title: str = None,
    ):
        self.button_list = button_list
        self.button_orientation = button_orientation
        self.markdown = markdown
        self.single_title = single_title
        self.single_url = single_url
        self.title = title

    def validate(self):
        if self.button_list:
            for k in self.button_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['buttonList'] = []
        if self.button_list is not None:
            for k in self.button_list:
                result['buttonList'].append(k.to_map() if k else None)
        if self.button_orientation is not None:
            result['buttonOrientation'] = self.button_orientation
        if self.markdown is not None:
            result['markdown'] = self.markdown
        if self.single_title is not None:
            result['singleTitle'] = self.single_title
        if self.single_url is not None:
            result['singleUrl'] = self.single_url
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.button_list = []
        if m.get('buttonList') is not None:
            for k in m.get('buttonList'):
                temp_model = BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList()
                self.button_list.append(temp_model.from_map(k))
        if m.get('buttonOrientation') is not None:
            self.button_orientation = m.get('buttonOrientation')
        if m.get('markdown') is not None:
            self.markdown = m.get('markdown')
        if m.get('singleTitle') is not None:
            self.single_title = m.get('singleTitle')
        if m.get('singleUrl') is not None:
            self.single_url = m.get('singleUrl')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyLink(TeaModel):
    def __init__(
        self,
        message_url: str = None,
        pic_url: str = None,
        text: str = None,
        title: str = None,
    ):
        self.message_url = message_url
        self.pic_url = pic_url
        self.text = text
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_url is not None:
            result['messageUrl'] = self.message_url
        if self.pic_url is not None:
            result['picUrl'] = self.pic_url
        if self.text is not None:
            result['text'] = self.text
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('messageUrl') is not None:
            self.message_url = m.get('messageUrl')
        if m.get('picUrl') is not None:
            self.pic_url = m.get('picUrl')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown(TeaModel):
    def __init__(
        self,
        text: str = None,
        title: str = None,
    ):
        self.text = text
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['text'] = self.text
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyText(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class BatchSendOfficialAccountOTOMessageRequestDetailMessageBody(TeaModel):
    def __init__(
        self,
        action_card: BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard = None,
        link: BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyLink = None,
        markdown: BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown = None,
        text: BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyText = None,
    ):
        self.action_card = action_card
        self.link = link
        self.markdown = markdown
        self.text = text

    def validate(self):
        if self.action_card:
            self.action_card.validate()
        if self.link:
            self.link.validate()
        if self.markdown:
            self.markdown.validate()
        if self.text:
            self.text.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_card is not None:
            result['actionCard'] = self.action_card.to_map()
        if self.link is not None:
            result['link'] = self.link.to_map()
        if self.markdown is not None:
            result['markdown'] = self.markdown.to_map()
        if self.text is not None:
            result['text'] = self.text.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionCard') is not None:
            temp_model = BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard()
            self.action_card = temp_model.from_map(m['actionCard'])
        if m.get('link') is not None:
            temp_model = BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyLink()
            self.link = temp_model.from_map(m['link'])
        if m.get('markdown') is not None:
            temp_model = BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown()
            self.markdown = temp_model.from_map(m['markdown'])
        if m.get('text') is not None:
            temp_model = BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyText()
            self.text = temp_model.from_map(m['text'])
        return self


class BatchSendOfficialAccountOTOMessageRequestDetail(TeaModel):
    def __init__(
        self,
        biz_request_id: str = None,
        message_body: BatchSendOfficialAccountOTOMessageRequestDetailMessageBody = None,
        msg_type: str = None,
        send_to_all: bool = None,
        user_id_list: List[str] = None,
        uuid: str = None,
    ):
        self.biz_request_id = biz_request_id
        self.message_body = message_body
        self.msg_type = msg_type
        self.send_to_all = send_to_all
        self.user_id_list = user_id_list
        self.uuid = uuid

    def validate(self):
        if self.message_body:
            self.message_body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_request_id is not None:
            result['bizRequestId'] = self.biz_request_id
        if self.message_body is not None:
            result['messageBody'] = self.message_body.to_map()
        if self.msg_type is not None:
            result['msgType'] = self.msg_type
        if self.send_to_all is not None:
            result['sendToAll'] = self.send_to_all
        if self.user_id_list is not None:
            result['userIdList'] = self.user_id_list
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizRequestId') is not None:
            self.biz_request_id = m.get('bizRequestId')
        if m.get('messageBody') is not None:
            temp_model = BatchSendOfficialAccountOTOMessageRequestDetailMessageBody()
            self.message_body = temp_model.from_map(m['messageBody'])
        if m.get('msgType') is not None:
            self.msg_type = m.get('msgType')
        if m.get('sendToAll') is not None:
            self.send_to_all = m.get('sendToAll')
        if m.get('userIdList') is not None:
            self.user_id_list = m.get('userIdList')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class BatchSendOfficialAccountOTOMessageRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        biz_id: str = None,
        detail: BatchSendOfficialAccountOTOMessageRequestDetail = None,
    ):
        self.account_id = account_id
        self.biz_id = biz_id
        self.detail = detail

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.detail is not None:
            result['detail'] = self.detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('detail') is not None:
            temp_model = BatchSendOfficialAccountOTOMessageRequestDetail()
            self.detail = temp_model.from_map(m['detail'])
        return self


class BatchSendOfficialAccountOTOMessageResponseBodyResult(TeaModel):
    def __init__(
        self,
        open_push_id: str = None,
    ):
        self.open_push_id = open_push_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_push_id is not None:
            result['openPushId'] = self.open_push_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openPushId') is not None:
            self.open_push_id = m.get('openPushId')
        return self


class BatchSendOfficialAccountOTOMessageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: BatchSendOfficialAccountOTOMessageResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = BatchSendOfficialAccountOTOMessageResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class BatchSendOfficialAccountOTOMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchSendOfficialAccountOTOMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchSendOfficialAccountOTOMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateContactsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class BatchUpdateContactsRequestRelationListBizDataList(TeaModel):
    def __init__(
        self,
        extend_value: str = None,
        key: str = None,
        value: str = None,
    ):
        self.extend_value = extend_value
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_value is not None:
            result['extendValue'] = self.extend_value
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extendValue') is not None:
            self.extend_value = m.get('extendValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class BatchUpdateContactsRequestRelationList(TeaModel):
    def __init__(
        self,
        biz_data_list: List[BatchUpdateContactsRequestRelationListBizDataList] = None,
        biz_ext_map: Dict[str, str] = None,
        relation_id: str = None,
    ):
        self.biz_data_list = biz_data_list
        self.biz_ext_map = biz_ext_map
        self.relation_id = relation_id

    def validate(self):
        if self.biz_data_list:
            for k in self.biz_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['bizDataList'] = []
        if self.biz_data_list is not None:
            for k in self.biz_data_list:
                result['bizDataList'].append(k.to_map() if k else None)
        if self.biz_ext_map is not None:
            result['bizExtMap'] = self.biz_ext_map
        if self.relation_id is not None:
            result['relationId'] = self.relation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_data_list = []
        if m.get('bizDataList') is not None:
            for k in m.get('bizDataList'):
                temp_model = BatchUpdateContactsRequestRelationListBizDataList()
                self.biz_data_list.append(temp_model.from_map(k))
        if m.get('bizExtMap') is not None:
            self.biz_ext_map = m.get('bizExtMap')
        if m.get('relationId') is not None:
            self.relation_id = m.get('relationId')
        return self


class BatchUpdateContactsRequest(TeaModel):
    def __init__(
        self,
        operator_user_id: str = None,
        relation_list: List[BatchUpdateContactsRequestRelationList] = None,
    ):
        self.operator_user_id = operator_user_id
        self.relation_list = relation_list

    def validate(self):
        if self.relation_list:
            for k in self.relation_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_user_id is not None:
            result['operatorUserId'] = self.operator_user_id
        result['relationList'] = []
        if self.relation_list is not None:
            for k in self.relation_list:
                result['relationList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operatorUserId') is not None:
            self.operator_user_id = m.get('operatorUserId')
        self.relation_list = []
        if m.get('relationList') is not None:
            for k in m.get('relationList'):
                temp_model = BatchUpdateContactsRequestRelationList()
                self.relation_list.append(temp_model.from_map(k))
        return self


class BatchUpdateContactsResponseBodyResults(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        relation_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.relation_id = relation_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.relation_id is not None:
            result['relationId'] = self.relation_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('relationId') is not None:
            self.relation_id = m.get('relationId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BatchUpdateContactsResponseBody(TeaModel):
    def __init__(
        self,
        results: List[BatchUpdateContactsResponseBodyResults] = None,
    ):
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = BatchUpdateContactsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchUpdateContactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchUpdateContactsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchUpdateContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateFollowRecordsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class BatchUpdateFollowRecordsRequestInstanceListDataArray(TeaModel):
    def __init__(
        self,
        extend_value: str = None,
        key: str = None,
        value: str = None,
    ):
        self.extend_value = extend_value
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_value is not None:
            result['extendValue'] = self.extend_value
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extendValue') is not None:
            self.extend_value = m.get('extendValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class BatchUpdateFollowRecordsRequestInstanceList(TeaModel):
    def __init__(
        self,
        data_array: List[BatchUpdateFollowRecordsRequestInstanceListDataArray] = None,
        instance_id: str = None,
    ):
        self.data_array = data_array
        self.instance_id = instance_id

    def validate(self):
        if self.data_array:
            for k in self.data_array:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dataArray'] = []
        if self.data_array is not None:
            for k in self.data_array:
                result['dataArray'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_array = []
        if m.get('dataArray') is not None:
            for k in m.get('dataArray'):
                temp_model = BatchUpdateFollowRecordsRequestInstanceListDataArray()
                self.data_array.append(temp_model.from_map(k))
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class BatchUpdateFollowRecordsRequest(TeaModel):
    def __init__(
        self,
        instance_list: List[BatchUpdateFollowRecordsRequestInstanceList] = None,
        operator_user_id: str = None,
    ):
        self.instance_list = instance_list
        self.operator_user_id = operator_user_id

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['instanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['instanceList'].append(k.to_map() if k else None)
        if self.operator_user_id is not None:
            result['operatorUserId'] = self.operator_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_list = []
        if m.get('instanceList') is not None:
            for k in m.get('instanceList'):
                temp_model = BatchUpdateFollowRecordsRequestInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        if m.get('operatorUserId') is not None:
            self.operator_user_id = m.get('operatorUserId')
        return self


class BatchUpdateFollowRecordsResponseBodyResults(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        instance_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.instance_id = instance_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BatchUpdateFollowRecordsResponseBody(TeaModel):
    def __init__(
        self,
        results: List[BatchUpdateFollowRecordsResponseBodyResults] = None,
    ):
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = BatchUpdateFollowRecordsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchUpdateFollowRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchUpdateFollowRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchUpdateFollowRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateRelationDatasHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class BatchUpdateRelationDatasRequestRelationListBizDataList(TeaModel):
    def __init__(
        self,
        extend_value: str = None,
        key: str = None,
        value: str = None,
    ):
        self.extend_value = extend_value
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_value is not None:
            result['extendValue'] = self.extend_value
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extendValue') is not None:
            self.extend_value = m.get('extendValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class BatchUpdateRelationDatasRequestRelationList(TeaModel):
    def __init__(
        self,
        biz_data_list: List[BatchUpdateRelationDatasRequestRelationListBizDataList] = None,
        biz_ext_map: Dict[str, str] = None,
        relation_id: str = None,
    ):
        self.biz_data_list = biz_data_list
        self.biz_ext_map = biz_ext_map
        self.relation_id = relation_id

    def validate(self):
        if self.biz_data_list:
            for k in self.biz_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['bizDataList'] = []
        if self.biz_data_list is not None:
            for k in self.biz_data_list:
                result['bizDataList'].append(k.to_map() if k else None)
        if self.biz_ext_map is not None:
            result['bizExtMap'] = self.biz_ext_map
        if self.relation_id is not None:
            result['relationId'] = self.relation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_data_list = []
        if m.get('bizDataList') is not None:
            for k in m.get('bizDataList'):
                temp_model = BatchUpdateRelationDatasRequestRelationListBizDataList()
                self.biz_data_list.append(temp_model.from_map(k))
        if m.get('bizExtMap') is not None:
            self.biz_ext_map = m.get('bizExtMap')
        if m.get('relationId') is not None:
            self.relation_id = m.get('relationId')
        return self


class BatchUpdateRelationDatasRequest(TeaModel):
    def __init__(
        self,
        operator_user_id: str = None,
        relation_list: List[BatchUpdateRelationDatasRequestRelationList] = None,
        relation_type: str = None,
        skip_duplicate_check: bool = None,
    ):
        self.operator_user_id = operator_user_id
        self.relation_list = relation_list
        self.relation_type = relation_type
        self.skip_duplicate_check = skip_duplicate_check

    def validate(self):
        if self.relation_list:
            for k in self.relation_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_user_id is not None:
            result['operatorUserId'] = self.operator_user_id
        result['relationList'] = []
        if self.relation_list is not None:
            for k in self.relation_list:
                result['relationList'].append(k.to_map() if k else None)
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        if self.skip_duplicate_check is not None:
            result['skipDuplicateCheck'] = self.skip_duplicate_check
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operatorUserId') is not None:
            self.operator_user_id = m.get('operatorUserId')
        self.relation_list = []
        if m.get('relationList') is not None:
            for k in m.get('relationList'):
                temp_model = BatchUpdateRelationDatasRequestRelationList()
                self.relation_list.append(temp_model.from_map(k))
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        if m.get('skipDuplicateCheck') is not None:
            self.skip_duplicate_check = m.get('skipDuplicateCheck')
        return self


class BatchUpdateRelationDatasResponseBodyResults(TeaModel):
    def __init__(
        self,
        duplicated_relation_ids: List[str] = None,
        error_code: str = None,
        error_msg: str = None,
        relation_id: str = None,
        success: bool = None,
    ):
        self.duplicated_relation_ids = duplicated_relation_ids
        self.error_code = error_code
        self.error_msg = error_msg
        self.relation_id = relation_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duplicated_relation_ids is not None:
            result['duplicatedRelationIds'] = self.duplicated_relation_ids
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.relation_id is not None:
            result['relationId'] = self.relation_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duplicatedRelationIds') is not None:
            self.duplicated_relation_ids = m.get('duplicatedRelationIds')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('relationId') is not None:
            self.relation_id = m.get('relationId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BatchUpdateRelationDatasResponseBody(TeaModel):
    def __init__(
        self,
        results: List[BatchUpdateRelationDatasResponseBodyResults] = None,
    ):
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = BatchUpdateRelationDatasResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchUpdateRelationDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchUpdateRelationDatasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchUpdateRelationDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomerHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class CreateCustomerRequestContacts(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        extend_data: Dict[str, Any] = None,
    ):
        self.data = data
        self.extend_data = extend_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.extend_data is not None:
            result['extendData'] = self.extend_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('extendData') is not None:
            self.extend_data = m.get('extendData')
        return self


class CreateCustomerRequestPermission(TeaModel):
    def __init__(
        self,
        owner_staff_ids: List[str] = None,
        participant_staff_ids: List[str] = None,
    ):
        self.owner_staff_ids = owner_staff_ids
        self.participant_staff_ids = participant_staff_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_staff_ids is not None:
            result['ownerStaffIds'] = self.owner_staff_ids
        if self.participant_staff_ids is not None:
            result['participantStaffIds'] = self.participant_staff_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ownerStaffIds') is not None:
            self.owner_staff_ids = m.get('ownerStaffIds')
        if m.get('participantStaffIds') is not None:
            self.participant_staff_ids = m.get('participantStaffIds')
        return self


class CreateCustomerRequestSaveOption(TeaModel):
    def __init__(
        self,
        customer_existed_policy: str = None,
        skip_duplicate_check: bool = None,
        subscribe_policy: int = None,
        throw_exception_while_saving_contact_failed: bool = None,
    ):
        self.customer_existed_policy = customer_existed_policy
        self.skip_duplicate_check = skip_duplicate_check
        self.subscribe_policy = subscribe_policy
        self.throw_exception_while_saving_contact_failed = throw_exception_while_saving_contact_failed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_existed_policy is not None:
            result['customerExistedPolicy'] = self.customer_existed_policy
        if self.skip_duplicate_check is not None:
            result['skipDuplicateCheck'] = self.skip_duplicate_check
        if self.subscribe_policy is not None:
            result['subscribePolicy'] = self.subscribe_policy
        if self.throw_exception_while_saving_contact_failed is not None:
            result['throwExceptionWhileSavingContactFailed'] = self.throw_exception_while_saving_contact_failed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customerExistedPolicy') is not None:
            self.customer_existed_policy = m.get('customerExistedPolicy')
        if m.get('skipDuplicateCheck') is not None:
            self.skip_duplicate_check = m.get('skipDuplicateCheck')
        if m.get('subscribePolicy') is not None:
            self.subscribe_policy = m.get('subscribePolicy')
        if m.get('throwExceptionWhileSavingContactFailed') is not None:
            self.throw_exception_while_saving_contact_failed = m.get('throwExceptionWhileSavingContactFailed')
        return self


class CreateCustomerRequest(TeaModel):
    def __init__(
        self,
        contacts: List[CreateCustomerRequestContacts] = None,
        creator_user_id: str = None,
        data: Dict[str, Any] = None,
        extend_data: Dict[str, Any] = None,
        instance_id: str = None,
        object_type: str = None,
        permission: CreateCustomerRequestPermission = None,
        save_option: CreateCustomerRequestSaveOption = None,
    ):
        self.contacts = contacts
        self.creator_user_id = creator_user_id
        self.data = data
        self.extend_data = extend_data
        self.instance_id = instance_id
        self.object_type = object_type
        self.permission = permission
        self.save_option = save_option

    def validate(self):
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()
        if self.permission:
            self.permission.validate()
        if self.save_option:
            self.save_option.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['contacts'].append(k.to_map() if k else None)
        if self.creator_user_id is not None:
            result['creatorUserId'] = self.creator_user_id
        if self.data is not None:
            result['data'] = self.data
        if self.extend_data is not None:
            result['extendData'] = self.extend_data
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.object_type is not None:
            result['objectType'] = self.object_type
        if self.permission is not None:
            result['permission'] = self.permission.to_map()
        if self.save_option is not None:
            result['saveOption'] = self.save_option.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contacts = []
        if m.get('contacts') is not None:
            for k in m.get('contacts'):
                temp_model = CreateCustomerRequestContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('creatorUserId') is not None:
            self.creator_user_id = m.get('creatorUserId')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('extendData') is not None:
            self.extend_data = m.get('extendData')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        if m.get('permission') is not None:
            temp_model = CreateCustomerRequestPermission()
            self.permission = temp_model.from_map(m['permission'])
        if m.get('saveOption') is not None:
            temp_model = CreateCustomerRequestSaveOption()
            self.save_option = temp_model.from_map(m['saveOption'])
        return self


class CreateCustomerResponseBodyContacts(TeaModel):
    def __init__(
        self,
        contact_instance_id: str = None,
    ):
        self.contact_instance_id = contact_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_instance_id is not None:
            result['contactInstanceId'] = self.contact_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactInstanceId') is not None:
            self.contact_instance_id = m.get('contactInstanceId')
        return self


class CreateCustomerResponseBody(TeaModel):
    def __init__(
        self,
        contacts: List[CreateCustomerResponseBodyContacts] = None,
        customer_instance_id: str = None,
        object_type: str = None,
    ):
        self.contacts = contacts
        self.customer_instance_id = customer_instance_id
        self.object_type = object_type

    def validate(self):
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['contacts'].append(k.to_map() if k else None)
        if self.customer_instance_id is not None:
            result['customerInstanceId'] = self.customer_instance_id
        if self.object_type is not None:
            result['objectType'] = self.object_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contacts = []
        if m.get('contacts') is not None:
            for k in m.get('contacts'):
                temp_model = CreateCustomerResponseBodyContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('customerInstanceId') is not None:
            self.customer_instance_id = m.get('customerInstanceId')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        return self


class CreateCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class CreateGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        member_user_ids: str = None,
        owner_user_id: str = None,
        relation_type: str = None,
    ):
        self.group_name = group_name
        self.member_user_ids = member_user_ids
        self.owner_user_id = owner_user_id
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.member_user_ids is not None:
            result['memberUserIds'] = self.member_user_ids
        if self.owner_user_id is not None:
            result['ownerUserId'] = self.owner_user_id
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('memberUserIds') is not None:
            self.member_user_ids = m.get('memberUserIds')
        if m.get('ownerUserId') is not None:
            self.owner_user_id = m.get('ownerUserId')
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(
        self,
        open_conversation_id: str = None,
    ):
        self.open_conversation_id = open_conversation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupSetHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class CreateGroupSetRequest(TeaModel):
    def __init__(
        self,
        creator_user_id: str = None,
        manager_user_ids: str = None,
        member_quota: int = None,
        name: str = None,
        notice: str = None,
        notice_toped: int = None,
        owner_user_id: str = None,
        relation_type: str = None,
        template_id: str = None,
        welcome: str = None,
    ):
        self.creator_user_id = creator_user_id
        self.manager_user_ids = manager_user_ids
        self.member_quota = member_quota
        self.name = name
        self.notice = notice
        self.notice_toped = notice_toped
        self.owner_user_id = owner_user_id
        self.relation_type = relation_type
        self.template_id = template_id
        self.welcome = welcome

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_user_id is not None:
            result['creatorUserId'] = self.creator_user_id
        if self.manager_user_ids is not None:
            result['managerUserIds'] = self.manager_user_ids
        if self.member_quota is not None:
            result['memberQuota'] = self.member_quota
        if self.name is not None:
            result['name'] = self.name
        if self.notice is not None:
            result['notice'] = self.notice
        if self.notice_toped is not None:
            result['noticeToped'] = self.notice_toped
        if self.owner_user_id is not None:
            result['ownerUserId'] = self.owner_user_id
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.welcome is not None:
            result['welcome'] = self.welcome
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorUserId') is not None:
            self.creator_user_id = m.get('creatorUserId')
        if m.get('managerUserIds') is not None:
            self.manager_user_ids = m.get('managerUserIds')
        if m.get('memberQuota') is not None:
            self.member_quota = m.get('memberQuota')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('notice') is not None:
            self.notice = m.get('notice')
        if m.get('noticeToped') is not None:
            self.notice_toped = m.get('noticeToped')
        if m.get('ownerUserId') is not None:
            self.owner_user_id = m.get('ownerUserId')
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('welcome') is not None:
            self.welcome = m.get('welcome')
        return self


class CreateGroupSetResponseBodyManager(TeaModel):
    def __init__(
        self,
        name: str = None,
        user_id: str = None,
    ):
        self.name = name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateGroupSetResponseBodyOwner(TeaModel):
    def __init__(
        self,
        name: str = None,
        user_id: str = None,
    ):
        self.name = name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateGroupSetResponseBody(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        invite_link: str = None,
        last_open_conversation_id: str = None,
        manager: List[CreateGroupSetResponseBodyManager] = None,
        manager_user_ids: str = None,
        member_count: int = None,
        member_quota: int = None,
        name: str = None,
        notice: str = None,
        notice_toped: int = None,
        open_group_set_id: str = None,
        owner: CreateGroupSetResponseBodyOwner = None,
        owner_user_id: str = None,
        relation_type: str = None,
        template_id: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.invite_link = invite_link
        self.last_open_conversation_id = last_open_conversation_id
        self.manager = manager
        self.manager_user_ids = manager_user_ids
        self.member_count = member_count
        self.member_quota = member_quota
        self.name = name
        self.notice = notice
        self.notice_toped = notice_toped
        self.open_group_set_id = open_group_set_id
        self.owner = owner
        self.owner_user_id = owner_user_id
        self.relation_type = relation_type
        self.template_id = template_id

    def validate(self):
        if self.manager:
            for k in self.manager:
                if k:
                    k.validate()
        if self.owner:
            self.owner.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.invite_link is not None:
            result['inviteLink'] = self.invite_link
        if self.last_open_conversation_id is not None:
            result['lastOpenConversationId'] = self.last_open_conversation_id
        result['manager'] = []
        if self.manager is not None:
            for k in self.manager:
                result['manager'].append(k.to_map() if k else None)
        if self.manager_user_ids is not None:
            result['managerUserIds'] = self.manager_user_ids
        if self.member_count is not None:
            result['memberCount'] = self.member_count
        if self.member_quota is not None:
            result['memberQuota'] = self.member_quota
        if self.name is not None:
            result['name'] = self.name
        if self.notice is not None:
            result['notice'] = self.notice
        if self.notice_toped is not None:
            result['noticeToped'] = self.notice_toped
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.owner is not None:
            result['owner'] = self.owner.to_map()
        if self.owner_user_id is not None:
            result['ownerUserId'] = self.owner_user_id
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('inviteLink') is not None:
            self.invite_link = m.get('inviteLink')
        if m.get('lastOpenConversationId') is not None:
            self.last_open_conversation_id = m.get('lastOpenConversationId')
        self.manager = []
        if m.get('manager') is not None:
            for k in m.get('manager'):
                temp_model = CreateGroupSetResponseBodyManager()
                self.manager.append(temp_model.from_map(k))
        if m.get('managerUserIds') is not None:
            self.manager_user_ids = m.get('managerUserIds')
        if m.get('memberCount') is not None:
            self.member_count = m.get('memberCount')
        if m.get('memberQuota') is not None:
            self.member_quota = m.get('memberQuota')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('notice') is not None:
            self.notice = m.get('notice')
        if m.get('noticeToped') is not None:
            self.notice_toped = m.get('noticeToped')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('owner') is not None:
            temp_model = CreateGroupSetResponseBodyOwner()
            self.owner = temp_model.from_map(m['owner'])
        if m.get('ownerUserId') is not None:
            self.owner_user_id = m.get('ownerUserId')
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class CreateGroupSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGroupSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateGroupSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRelationMetaHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class CreateRelationMetaRequestRelationMetaDTOItemsPropsOptions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateRelationMetaRequestRelationMetaDTOItemsProps(TeaModel):
    def __init__(
        self,
        align: str = None,
        biz_alias: str = None,
        choice: int = None,
        content: str = None,
        disabled: bool = None,
        duration: bool = None,
        field_id: str = None,
        format: str = None,
        invisible: bool = None,
        label: str = None,
        label_editable_freeze: bool = None,
        link: str = None,
        need_detail: str = None,
        not_print: str = None,
        not_upper: str = None,
        options: List[CreateRelationMetaRequestRelationMetaDTOItemsPropsOptions] = None,
        pay_enable: bool = None,
        placeholder: str = None,
        required: bool = None,
        required_editable_freeze: bool = None,
        sortable: bool = None,
        unit: str = None,
    ):
        self.align = align
        self.biz_alias = biz_alias
        self.choice = choice
        self.content = content
        self.disabled = disabled
        self.duration = duration
        self.field_id = field_id
        self.format = format
        self.invisible = invisible
        self.label = label
        self.label_editable_freeze = label_editable_freeze
        self.link = link
        self.need_detail = need_detail
        self.not_print = not_print
        self.not_upper = not_upper
        self.options = options
        self.pay_enable = pay_enable
        self.placeholder = placeholder
        self.required = required
        self.required_editable_freeze = required_editable_freeze
        self.sortable = sortable
        self.unit = unit

    def validate(self):
        if self.options:
            for k in self.options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align is not None:
            result['align'] = self.align
        if self.biz_alias is not None:
            result['bizAlias'] = self.biz_alias
        if self.choice is not None:
            result['choice'] = self.choice
        if self.content is not None:
            result['content'] = self.content
        if self.disabled is not None:
            result['disabled'] = self.disabled
        if self.duration is not None:
            result['duration'] = self.duration
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.format is not None:
            result['format'] = self.format
        if self.invisible is not None:
            result['invisible'] = self.invisible
        if self.label is not None:
            result['label'] = self.label
        if self.label_editable_freeze is not None:
            result['labelEditableFreeze'] = self.label_editable_freeze
        if self.link is not None:
            result['link'] = self.link
        if self.need_detail is not None:
            result['needDetail'] = self.need_detail
        if self.not_print is not None:
            result['notPrint'] = self.not_print
        if self.not_upper is not None:
            result['notUpper'] = self.not_upper
        result['options'] = []
        if self.options is not None:
            for k in self.options:
                result['options'].append(k.to_map() if k else None)
        if self.pay_enable is not None:
            result['payEnable'] = self.pay_enable
        if self.placeholder is not None:
            result['placeholder'] = self.placeholder
        if self.required is not None:
            result['required'] = self.required
        if self.required_editable_freeze is not None:
            result['requiredEditableFreeze'] = self.required_editable_freeze
        if self.sortable is not None:
            result['sortable'] = self.sortable
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('align') is not None:
            self.align = m.get('align')
        if m.get('bizAlias') is not None:
            self.biz_alias = m.get('bizAlias')
        if m.get('choice') is not None:
            self.choice = m.get('choice')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('invisible') is not None:
            self.invisible = m.get('invisible')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('labelEditableFreeze') is not None:
            self.label_editable_freeze = m.get('labelEditableFreeze')
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('needDetail') is not None:
            self.need_detail = m.get('needDetail')
        if m.get('notPrint') is not None:
            self.not_print = m.get('notPrint')
        if m.get('notUpper') is not None:
            self.not_upper = m.get('notUpper')
        self.options = []
        if m.get('options') is not None:
            for k in m.get('options'):
                temp_model = CreateRelationMetaRequestRelationMetaDTOItemsPropsOptions()
                self.options.append(temp_model.from_map(k))
        if m.get('payEnable') is not None:
            self.pay_enable = m.get('payEnable')
        if m.get('placeholder') is not None:
            self.placeholder = m.get('placeholder')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('requiredEditableFreeze') is not None:
            self.required_editable_freeze = m.get('requiredEditableFreeze')
        if m.get('sortable') is not None:
            self.sortable = m.get('sortable')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class CreateRelationMetaRequestRelationMetaDTOItems(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        props: CreateRelationMetaRequestRelationMetaDTOItemsProps = None,
    ):
        self.component_name = component_name
        self.props = props

    def validate(self):
        if self.props:
            self.props.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.props is not None:
            result['props'] = self.props.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('props') is not None:
            temp_model = CreateRelationMetaRequestRelationMetaDTOItemsProps()
            self.props = temp_model.from_map(m['props'])
        return self


class CreateRelationMetaRequestRelationMetaDTO(TeaModel):
    def __init__(
        self,
        desc: str = None,
        items: List[CreateRelationMetaRequestRelationMetaDTOItems] = None,
        name: str = None,
        relation_type: str = None,
    ):
        self.desc = desc
        self.items = items
        self.name = name
        self.relation_type = relation_type

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = CreateRelationMetaRequestRelationMetaDTOItems()
                self.items.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        return self


class CreateRelationMetaRequest(TeaModel):
    def __init__(
        self,
        operator_user_id: str = None,
        relation_meta_dto: CreateRelationMetaRequestRelationMetaDTO = None,
        tenant: str = None,
    ):
        self.operator_user_id = operator_user_id
        self.relation_meta_dto = relation_meta_dto
        self.tenant = tenant

    def validate(self):
        if self.relation_meta_dto:
            self.relation_meta_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_user_id is not None:
            result['operatorUserId'] = self.operator_user_id
        if self.relation_meta_dto is not None:
            result['relationMetaDTO'] = self.relation_meta_dto.to_map()
        if self.tenant is not None:
            result['tenant'] = self.tenant
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operatorUserId') is not None:
            self.operator_user_id = m.get('operatorUserId')
        if m.get('relationMetaDTO') is not None:
            temp_model = CreateRelationMetaRequestRelationMetaDTO()
            self.relation_meta_dto = temp_model.from_map(m['relationMetaDTO'])
        if m.get('tenant') is not None:
            self.tenant = m.get('tenant')
        return self


class CreateRelationMetaResponseBody(TeaModel):
    def __init__(
        self,
        relation_type: str = None,
    ):
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        return self


class CreateRelationMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRelationMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRelationMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCrmCustomObjectDataHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class DeleteCrmCustomObjectDataRequest(TeaModel):
    def __init__(
        self,
        form_code: str = None,
    ):
        self.form_code = form_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form_code is not None:
            result['formCode'] = self.form_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('formCode') is not None:
            self.form_code = m.get('formCode')
        return self


class DeleteCrmCustomObjectDataResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class DeleteCrmCustomObjectDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCrmCustomObjectDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCrmCustomObjectDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCrmFormInstanceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class DeleteCrmFormInstanceRequest(TeaModel):
    def __init__(
        self,
        current_operator_user_id: str = None,
        name: str = None,
    ):
        self.current_operator_user_id = current_operator_user_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_operator_user_id is not None:
            result['currentOperatorUserId'] = self.current_operator_user_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentOperatorUserId') is not None:
            self.current_operator_user_id = m.get('currentOperatorUserId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DeleteCrmFormInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class DeleteCrmFormInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCrmFormInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCrmFormInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCrmPersonalCustomerHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class DeleteCrmPersonalCustomerRequest(TeaModel):
    def __init__(
        self,
        current_operator_user_id: str = None,
        relation_type: str = None,
    ):
        self.current_operator_user_id = current_operator_user_id
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_operator_user_id is not None:
            result['currentOperatorUserId'] = self.current_operator_user_id
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentOperatorUserId') is not None:
            self.current_operator_user_id = m.get('currentOperatorUserId')
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        return self


class DeleteCrmPersonalCustomerResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class DeleteCrmPersonalCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCrmPersonalCustomerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCrmPersonalCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLeadsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class DeleteLeadsRequest(TeaModel):
    def __init__(
        self,
        out_leads_ids: List[str] = None,
    ):
        self.out_leads_ids = out_leads_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_leads_ids is not None:
            result['outLeadsIds'] = self.out_leads_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('outLeadsIds') is not None:
            self.out_leads_ids = m.get('outLeadsIds')
        return self


class DeleteLeadsResponseBody(TeaModel):
    def __init__(
        self,
        out_leads_ids: List[str] = None,
    ):
        self.out_leads_ids = out_leads_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_leads_ids is not None:
            result['outLeadsIds'] = self.out_leads_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('outLeadsIds') is not None:
            self.out_leads_ids = m.get('outLeadsIds')
        return self


class DeleteLeadsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLeadsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteLeadsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRelationMetaFieldHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class DeleteRelationMetaFieldRequest(TeaModel):
    def __init__(
        self,
        field_id_list: List[str] = None,
        operator_user_id: str = None,
        relation_type: str = None,
        tenant: str = None,
    ):
        self.field_id_list = field_id_list
        self.operator_user_id = operator_user_id
        self.relation_type = relation_type
        self.tenant = tenant

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id_list is not None:
            result['fieldIdList'] = self.field_id_list
        if self.operator_user_id is not None:
            result['operatorUserId'] = self.operator_user_id
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        if self.tenant is not None:
            result['tenant'] = self.tenant
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldIdList') is not None:
            self.field_id_list = m.get('fieldIdList')
        if m.get('operatorUserId') is not None:
            self.operator_user_id = m.get('operatorUserId')
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        if m.get('tenant') is not None:
            self.tenant = m.get('tenant')
        return self


class DeleteRelationMetaFieldResponseBody(TeaModel):
    def __init__(
        self,
        relation_type: str = None,
    ):
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        return self


class DeleteRelationMetaFieldResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRelationMetaFieldResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRelationMetaFieldResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCrmPersonalCustomerObjectMetaHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class DescribeCrmPersonalCustomerObjectMetaRequest(TeaModel):
    def __init__(
        self,
        relation_type: str = None,
    ):
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        return self


class DescribeCrmPersonalCustomerObjectMetaResponseBodyFieldsReferenceFieldsSelectOptions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeCrmPersonalCustomerObjectMetaResponseBodyFieldsReferenceFields(TeaModel):
    def __init__(
        self,
        format: str = None,
        label: str = None,
        name: str = None,
        nillable: bool = None,
        select_options: List[DescribeCrmPersonalCustomerObjectMetaResponseBodyFieldsReferenceFieldsSelectOptions] = None,
        type: str = None,
        unit: str = None,
    ):
        self.format = format
        self.label = label
        self.name = name
        self.nillable = nillable
        self.select_options = select_options
        self.type = type
        self.unit = unit

    def validate(self):
        if self.select_options:
            for k in self.select_options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['format'] = self.format
        if self.label is not None:
            result['label'] = self.label
        if self.name is not None:
            result['name'] = self.name
        if self.nillable is not None:
            result['nillable'] = self.nillable
        result['selectOptions'] = []
        if self.select_options is not None:
            for k in self.select_options:
                result['selectOptions'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nillable') is not None:
            self.nillable = m.get('nillable')
        self.select_options = []
        if m.get('selectOptions') is not None:
            for k in m.get('selectOptions'):
                temp_model = DescribeCrmPersonalCustomerObjectMetaResponseBodyFieldsReferenceFieldsSelectOptions()
                self.select_options.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class DescribeCrmPersonalCustomerObjectMetaResponseBodyFieldsRollUpSummaryFields(TeaModel):
    def __init__(
        self,
        aggregator: str = None,
        name: str = None,
    ):
        self.aggregator = aggregator
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator is not None:
            result['aggregator'] = self.aggregator
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggregator') is not None:
            self.aggregator = m.get('aggregator')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeCrmPersonalCustomerObjectMetaResponseBodyFieldsSelectOptions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeCrmPersonalCustomerObjectMetaResponseBodyFields(TeaModel):
    def __init__(
        self,
        customized: bool = None,
        format: str = None,
        label: str = None,
        name: str = None,
        nillable: bool = None,
        quote: bool = None,
        reference_fields: List[DescribeCrmPersonalCustomerObjectMetaResponseBodyFieldsReferenceFields] = None,
        reference_to: str = None,
        roll_up_summary_fields: List[DescribeCrmPersonalCustomerObjectMetaResponseBodyFieldsRollUpSummaryFields] = None,
        select_options: List[DescribeCrmPersonalCustomerObjectMetaResponseBodyFieldsSelectOptions] = None,
        type: str = None,
        unit: str = None,
    ):
        self.customized = customized
        self.format = format
        self.label = label
        self.name = name
        self.nillable = nillable
        self.quote = quote
        self.reference_fields = reference_fields
        self.reference_to = reference_to
        self.roll_up_summary_fields = roll_up_summary_fields
        self.select_options = select_options
        self.type = type
        self.unit = unit

    def validate(self):
        if self.reference_fields:
            for k in self.reference_fields:
                if k:
                    k.validate()
        if self.roll_up_summary_fields:
            for k in self.roll_up_summary_fields:
                if k:
                    k.validate()
        if self.select_options:
            for k in self.select_options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customized is not None:
            result['customized'] = self.customized
        if self.format is not None:
            result['format'] = self.format
        if self.label is not None:
            result['label'] = self.label
        if self.name is not None:
            result['name'] = self.name
        if self.nillable is not None:
            result['nillable'] = self.nillable
        if self.quote is not None:
            result['quote'] = self.quote
        result['referenceFields'] = []
        if self.reference_fields is not None:
            for k in self.reference_fields:
                result['referenceFields'].append(k.to_map() if k else None)
        if self.reference_to is not None:
            result['referenceTo'] = self.reference_to
        result['rollUpSummaryFields'] = []
        if self.roll_up_summary_fields is not None:
            for k in self.roll_up_summary_fields:
                result['rollUpSummaryFields'].append(k.to_map() if k else None)
        result['selectOptions'] = []
        if self.select_options is not None:
            for k in self.select_options:
                result['selectOptions'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customized') is not None:
            self.customized = m.get('customized')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nillable') is not None:
            self.nillable = m.get('nillable')
        if m.get('quote') is not None:
            self.quote = m.get('quote')
        self.reference_fields = []
        if m.get('referenceFields') is not None:
            for k in m.get('referenceFields'):
                temp_model = DescribeCrmPersonalCustomerObjectMetaResponseBodyFieldsReferenceFields()
                self.reference_fields.append(temp_model.from_map(k))
        if m.get('referenceTo') is not None:
            self.reference_to = m.get('referenceTo')
        self.roll_up_summary_fields = []
        if m.get('rollUpSummaryFields') is not None:
            for k in m.get('rollUpSummaryFields'):
                temp_model = DescribeCrmPersonalCustomerObjectMetaResponseBodyFieldsRollUpSummaryFields()
                self.roll_up_summary_fields.append(temp_model.from_map(k))
        self.select_options = []
        if m.get('selectOptions') is not None:
            for k in m.get('selectOptions'):
                temp_model = DescribeCrmPersonalCustomerObjectMetaResponseBodyFieldsSelectOptions()
                self.select_options.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class DescribeCrmPersonalCustomerObjectMetaResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        customized: bool = None,
        fields: List[DescribeCrmPersonalCustomerObjectMetaResponseBodyFields] = None,
        name: str = None,
        status: str = None,
    ):
        self.code = code
        self.customized = customized
        self.fields = fields
        self.name = name
        self.status = status

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.customized is not None:
            result['customized'] = self.customized
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('customized') is not None:
            self.customized = m.get('customized')
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = DescribeCrmPersonalCustomerObjectMetaResponseBodyFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeCrmPersonalCustomerObjectMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCrmPersonalCustomerObjectMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCrmPersonalCustomerObjectMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRelationMetaHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class DescribeRelationMetaRequest(TeaModel):
    def __init__(
        self,
        operator_user_id: str = None,
        relation_types: List[str] = None,
        tenant: str = None,
    ):
        self.operator_user_id = operator_user_id
        self.relation_types = relation_types
        self.tenant = tenant

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_user_id is not None:
            result['operatorUserId'] = self.operator_user_id
        if self.relation_types is not None:
            result['relationTypes'] = self.relation_types
        if self.tenant is not None:
            result['tenant'] = self.tenant
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operatorUserId') is not None:
            self.operator_user_id = m.get('operatorUserId')
        if m.get('relationTypes') is not None:
            self.relation_types = m.get('relationTypes')
        if m.get('tenant') is not None:
            self.tenant = m.get('tenant')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsAvailableTemplates(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsDataSourceParamsFilters(TeaModel):
    def __init__(
        self,
        field_id: str = None,
        filter_type: str = None,
        value: str = None,
        value_type: str = None,
    ):
        self.field_id = field_id
        self.filter_type = filter_type
        self.value = value
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.filter_type is not None:
            result['filterType'] = self.filter_type
        if self.value is not None:
            result['value'] = self.value
        if self.value_type is not None:
            result['valueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('filterType') is not None:
            self.filter_type = m.get('filterType')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsDataSourceParams(TeaModel):
    def __init__(
        self,
        filters: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsDataSourceParamsFilters] = None,
    ):
        self.filters = filters

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['filters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('filters') is not None:
            for k in m.get('filters'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsDataSourceParamsFilters()
                self.filters.append(temp_model.from_map(k))
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsDataSourceTarget(TeaModel):
    def __init__(
        self,
        app_type: int = None,
        app_uuid: str = None,
        biz_type: str = None,
        form_code: str = None,
    ):
        self.app_type = app_type
        self.app_uuid = app_uuid
        self.biz_type = biz_type
        self.form_code = form_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.app_uuid is not None:
            result['appUuid'] = self.app_uuid
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.form_code is not None:
            result['formCode'] = self.form_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('appUuid') is not None:
            self.app_uuid = m.get('appUuid')
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('formCode') is not None:
            self.form_code = m.get('formCode')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsDataSource(TeaModel):
    def __init__(
        self,
        params: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsDataSourceParams = None,
        target: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsDataSourceTarget = None,
        type: str = None,
    ):
        self.params = params
        self.target = target
        self.type = type

    def validate(self):
        if self.params:
            self.params.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['params'] = self.params.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('params') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsDataSourceParams()
            self.params = temp_model.from_map(m['params'])
        if m.get('target') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsDataSourceTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsFieldsRelatePropsOptionsExtension(TeaModel):
    def __init__(
        self,
        edit_freeze: bool = None,
    ):
        self.edit_freeze = edit_freeze

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edit_freeze is not None:
            result['editFreeze'] = self.edit_freeze
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('editFreeze') is not None:
            self.edit_freeze = m.get('editFreeze')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsFieldsRelatePropsOptions(TeaModel):
    def __init__(
        self,
        extension: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsFieldsRelatePropsOptionsExtension = None,
        key: str = None,
        value: str = None,
    ):
        self.extension = extension
        self.key = key
        self.value = value

    def validate(self):
        if self.extension:
            self.extension.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['extension'] = self.extension.to_map()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extension') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsFieldsRelatePropsOptionsExtension()
            self.extension = temp_model.from_map(m['extension'])
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsFieldsRelatePropsStatField(TeaModel):
    def __init__(
        self,
        field_id: str = None,
        label: str = None,
        unit: str = None,
        upper: bool = None,
    ):
        self.field_id = field_id
        self.label = label
        self.unit = unit
        self.upper = upper

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.label is not None:
            result['label'] = self.label
        if self.unit is not None:
            result['unit'] = self.unit
        if self.upper is not None:
            result['upper'] = self.upper
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('upper') is not None:
            self.upper = m.get('upper')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsFieldsRelateProps(TeaModel):
    def __init__(
        self,
        align: str = None,
        biz_alias: str = None,
        choice: int = None,
        content: str = None,
        disabled: bool = None,
        duration: bool = None,
        duration_label: str = None,
        field_id: str = None,
        format: str = None,
        formula: str = None,
        invisible: bool = None,
        label: str = None,
        label_editable_freeze: bool = None,
        limit: int = None,
        link: str = None,
        mode: str = None,
        not_upper: str = None,
        options: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsFieldsRelatePropsOptions] = None,
        pay_enable: bool = None,
        placeholder: str = None,
        ratio: int = None,
        required: bool = None,
        required_editable_freeze: bool = None,
        spread: bool = None,
        stat_field: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsFieldsRelatePropsStatField] = None,
        unit: str = None,
        vertical_print: bool = None,
        watermark: bool = None,
    ):
        self.align = align
        self.biz_alias = biz_alias
        self.choice = choice
        self.content = content
        self.disabled = disabled
        self.duration = duration
        self.duration_label = duration_label
        self.field_id = field_id
        self.format = format
        self.formula = formula
        self.invisible = invisible
        self.label = label
        self.label_editable_freeze = label_editable_freeze
        self.limit = limit
        self.link = link
        self.mode = mode
        self.not_upper = not_upper
        self.options = options
        self.pay_enable = pay_enable
        self.placeholder = placeholder
        self.ratio = ratio
        self.required = required
        self.required_editable_freeze = required_editable_freeze
        self.spread = spread
        self.stat_field = stat_field
        self.unit = unit
        self.vertical_print = vertical_print
        self.watermark = watermark

    def validate(self):
        if self.options:
            for k in self.options:
                if k:
                    k.validate()
        if self.stat_field:
            for k in self.stat_field:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align is not None:
            result['align'] = self.align
        if self.biz_alias is not None:
            result['bizAlias'] = self.biz_alias
        if self.choice is not None:
            result['choice'] = self.choice
        if self.content is not None:
            result['content'] = self.content
        if self.disabled is not None:
            result['disabled'] = self.disabled
        if self.duration is not None:
            result['duration'] = self.duration
        if self.duration_label is not None:
            result['durationLabel'] = self.duration_label
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.format is not None:
            result['format'] = self.format
        if self.formula is not None:
            result['formula'] = self.formula
        if self.invisible is not None:
            result['invisible'] = self.invisible
        if self.label is not None:
            result['label'] = self.label
        if self.label_editable_freeze is not None:
            result['labelEditableFreeze'] = self.label_editable_freeze
        if self.limit is not None:
            result['limit'] = self.limit
        if self.link is not None:
            result['link'] = self.link
        if self.mode is not None:
            result['mode'] = self.mode
        if self.not_upper is not None:
            result['notUpper'] = self.not_upper
        result['options'] = []
        if self.options is not None:
            for k in self.options:
                result['options'].append(k.to_map() if k else None)
        if self.pay_enable is not None:
            result['payEnable'] = self.pay_enable
        if self.placeholder is not None:
            result['placeholder'] = self.placeholder
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.required is not None:
            result['required'] = self.required
        if self.required_editable_freeze is not None:
            result['requiredEditableFreeze'] = self.required_editable_freeze
        if self.spread is not None:
            result['spread'] = self.spread
        result['statField'] = []
        if self.stat_field is not None:
            for k in self.stat_field:
                result['statField'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['unit'] = self.unit
        if self.vertical_print is not None:
            result['verticalPrint'] = self.vertical_print
        if self.watermark is not None:
            result['watermark'] = self.watermark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('align') is not None:
            self.align = m.get('align')
        if m.get('bizAlias') is not None:
            self.biz_alias = m.get('bizAlias')
        if m.get('choice') is not None:
            self.choice = m.get('choice')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('durationLabel') is not None:
            self.duration_label = m.get('durationLabel')
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('formula') is not None:
            self.formula = m.get('formula')
        if m.get('invisible') is not None:
            self.invisible = m.get('invisible')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('labelEditableFreeze') is not None:
            self.label_editable_freeze = m.get('labelEditableFreeze')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('notUpper') is not None:
            self.not_upper = m.get('notUpper')
        self.options = []
        if m.get('options') is not None:
            for k in m.get('options'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsFieldsRelatePropsOptions()
                self.options.append(temp_model.from_map(k))
        if m.get('payEnable') is not None:
            self.pay_enable = m.get('payEnable')
        if m.get('placeholder') is not None:
            self.placeholder = m.get('placeholder')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('requiredEditableFreeze') is not None:
            self.required_editable_freeze = m.get('requiredEditableFreeze')
        if m.get('spread') is not None:
            self.spread = m.get('spread')
        self.stat_field = []
        if m.get('statField') is not None:
            for k in m.get('statField'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsFieldsRelatePropsStatField()
                self.stat_field.append(temp_model.from_map(k))
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('verticalPrint') is not None:
            self.vertical_print = m.get('verticalPrint')
        if m.get('watermark') is not None:
            self.watermark = m.get('watermark')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsFields(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        relate_props: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsFieldsRelateProps = None,
    ):
        self.component_name = component_name
        self.relate_props = relate_props

    def validate(self):
        if self.relate_props:
            self.relate_props.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.relate_props is not None:
            result['relateProps'] = self.relate_props.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('relateProps') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsFieldsRelateProps()
            self.relate_props = temp_model.from_map(m['relateProps'])
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsOptionsExtension(TeaModel):
    def __init__(
        self,
        edit_freeze: bool = None,
    ):
        self.edit_freeze = edit_freeze

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edit_freeze is not None:
            result['editFreeze'] = self.edit_freeze
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('editFreeze') is not None:
            self.edit_freeze = m.get('editFreeze')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsOptions(TeaModel):
    def __init__(
        self,
        extension: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsOptionsExtension = None,
        key: str = None,
        value: str = None,
    ):
        self.extension = extension
        self.key = key
        self.value = value

    def validate(self):
        if self.extension:
            self.extension.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['extension'] = self.extension.to_map()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extension') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsOptionsExtension()
            self.extension = temp_model.from_map(m['extension'])
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceDataSourceParamsFilters(TeaModel):
    def __init__(
        self,
        field_id: str = None,
        filter_type: str = None,
        value: str = None,
        value_type: str = None,
    ):
        self.field_id = field_id
        self.filter_type = filter_type
        self.value = value
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.filter_type is not None:
            result['filterType'] = self.filter_type
        if self.value is not None:
            result['value'] = self.value
        if self.value_type is not None:
            result['valueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('filterType') is not None:
            self.filter_type = m.get('filterType')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceDataSourceParams(TeaModel):
    def __init__(
        self,
        filters: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceDataSourceParamsFilters] = None,
    ):
        self.filters = filters

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['filters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('filters') is not None:
            for k in m.get('filters'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceDataSourceParamsFilters()
                self.filters.append(temp_model.from_map(k))
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceDataSourceTarget(TeaModel):
    def __init__(
        self,
        app_type: int = None,
        app_uuid: str = None,
        biz_type: str = None,
        form_code: str = None,
    ):
        self.app_type = app_type
        self.app_uuid = app_uuid
        self.biz_type = biz_type
        self.form_code = form_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.app_uuid is not None:
            result['appUuid'] = self.app_uuid
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.form_code is not None:
            result['formCode'] = self.form_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('appUuid') is not None:
            self.app_uuid = m.get('appUuid')
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('formCode') is not None:
            self.form_code = m.get('formCode')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceDataSource(TeaModel):
    def __init__(
        self,
        params: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceDataSourceParams = None,
        target: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceDataSourceTarget = None,
        type: str = None,
    ):
        self.params = params
        self.target = target
        self.type = type

    def validate(self):
        if self.params:
            self.params.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['params'] = self.params.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('params') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceDataSourceParams()
            self.params = temp_model.from_map(m['params'])
        if m.get('target') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceDataSourceTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceFieldsRelatePropsOptions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceFieldsRelatePropsStatField(TeaModel):
    def __init__(
        self,
        field_id: str = None,
        label: str = None,
        unit: str = None,
        upper: bool = None,
    ):
        self.field_id = field_id
        self.label = label
        self.unit = unit
        self.upper = upper

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.label is not None:
            result['label'] = self.label
        if self.unit is not None:
            result['unit'] = self.unit
        if self.upper is not None:
            result['upper'] = self.upper
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('upper') is not None:
            self.upper = m.get('upper')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceFieldsRelateProps(TeaModel):
    def __init__(
        self,
        align: str = None,
        biz_alias: str = None,
        choice: int = None,
        content: str = None,
        disabled: bool = None,
        duration: str = None,
        field_id: str = None,
        format: str = None,
        formula: str = None,
        invisible: bool = None,
        label: str = None,
        label_editable_freeze: bool = None,
        link: str = None,
        multi: int = None,
        not_upper: str = None,
        options: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceFieldsRelatePropsOptions] = None,
        pay_enable: bool = None,
        placeholder: str = None,
        quote: int = None,
        required: bool = None,
        required_editable_freeze: bool = None,
        stat_field: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceFieldsRelatePropsStatField] = None,
        unit: str = None,
        vertical_print: bool = None,
    ):
        self.align = align
        self.biz_alias = biz_alias
        self.choice = choice
        self.content = content
        self.disabled = disabled
        self.duration = duration
        self.field_id = field_id
        self.format = format
        self.formula = formula
        self.invisible = invisible
        self.label = label
        self.label_editable_freeze = label_editable_freeze
        self.link = link
        self.multi = multi
        self.not_upper = not_upper
        self.options = options
        self.pay_enable = pay_enable
        self.placeholder = placeholder
        self.quote = quote
        self.required = required
        self.required_editable_freeze = required_editable_freeze
        self.stat_field = stat_field
        self.unit = unit
        self.vertical_print = vertical_print

    def validate(self):
        if self.options:
            for k in self.options:
                if k:
                    k.validate()
        if self.stat_field:
            for k in self.stat_field:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align is not None:
            result['align'] = self.align
        if self.biz_alias is not None:
            result['bizAlias'] = self.biz_alias
        if self.choice is not None:
            result['choice'] = self.choice
        if self.content is not None:
            result['content'] = self.content
        if self.disabled is not None:
            result['disabled'] = self.disabled
        if self.duration is not None:
            result['duration'] = self.duration
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.format is not None:
            result['format'] = self.format
        if self.formula is not None:
            result['formula'] = self.formula
        if self.invisible is not None:
            result['invisible'] = self.invisible
        if self.label is not None:
            result['label'] = self.label
        if self.label_editable_freeze is not None:
            result['labelEditableFreeze'] = self.label_editable_freeze
        if self.link is not None:
            result['link'] = self.link
        if self.multi is not None:
            result['multi'] = self.multi
        if self.not_upper is not None:
            result['notUpper'] = self.not_upper
        result['options'] = []
        if self.options is not None:
            for k in self.options:
                result['options'].append(k.to_map() if k else None)
        if self.pay_enable is not None:
            result['payEnable'] = self.pay_enable
        if self.placeholder is not None:
            result['placeholder'] = self.placeholder
        if self.quote is not None:
            result['quote'] = self.quote
        if self.required is not None:
            result['required'] = self.required
        if self.required_editable_freeze is not None:
            result['requiredEditableFreeze'] = self.required_editable_freeze
        result['statField'] = []
        if self.stat_field is not None:
            for k in self.stat_field:
                result['statField'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['unit'] = self.unit
        if self.vertical_print is not None:
            result['verticalPrint'] = self.vertical_print
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('align') is not None:
            self.align = m.get('align')
        if m.get('bizAlias') is not None:
            self.biz_alias = m.get('bizAlias')
        if m.get('choice') is not None:
            self.choice = m.get('choice')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('formula') is not None:
            self.formula = m.get('formula')
        if m.get('invisible') is not None:
            self.invisible = m.get('invisible')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('labelEditableFreeze') is not None:
            self.label_editable_freeze = m.get('labelEditableFreeze')
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('multi') is not None:
            self.multi = m.get('multi')
        if m.get('notUpper') is not None:
            self.not_upper = m.get('notUpper')
        self.options = []
        if m.get('options') is not None:
            for k in m.get('options'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceFieldsRelatePropsOptions()
                self.options.append(temp_model.from_map(k))
        if m.get('payEnable') is not None:
            self.pay_enable = m.get('payEnable')
        if m.get('placeholder') is not None:
            self.placeholder = m.get('placeholder')
        if m.get('quote') is not None:
            self.quote = m.get('quote')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('requiredEditableFreeze') is not None:
            self.required_editable_freeze = m.get('requiredEditableFreeze')
        self.stat_field = []
        if m.get('statField') is not None:
            for k in m.get('statField'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceFieldsRelatePropsStatField()
                self.stat_field.append(temp_model.from_map(k))
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('verticalPrint') is not None:
            self.vertical_print = m.get('verticalPrint')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceFields(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        relate_props: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceFieldsRelateProps = None,
    ):
        self.component_name = component_name
        self.relate_props = relate_props

    def validate(self):
        if self.relate_props:
            self.relate_props.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.relate_props is not None:
            result['relateProps'] = self.relate_props.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('relateProps') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceFieldsRelateProps()
            self.relate_props = temp_model.from_map(m['relateProps'])
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSource(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        data_source: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceDataSource = None,
        fields: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceFields] = None,
    ):
        self.biz_type = biz_type
        self.data_source = data_source
        self.fields = fields

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('dataSource') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceDataSource()
            self.data_source = temp_model.from_map(m['dataSource'])
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSourceFields()
                self.fields.append(temp_model.from_map(k))
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRule(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsStatField(TeaModel):
    def __init__(
        self,
        field_id: str = None,
        label: str = None,
        unit: str = None,
        upper: bool = None,
    ):
        self.field_id = field_id
        self.label = label
        self.unit = unit
        self.upper = upper

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.label is not None:
            result['label'] = self.label
        if self.unit is not None:
            result['unit'] = self.unit
        if self.upper is not None:
            result['upper'] = self.upper
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('upper') is not None:
            self.upper = m.get('upper')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenProps(TeaModel):
    def __init__(
        self,
        action_name: str = None,
        align: str = None,
        available_templates: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsAvailableTemplates] = None,
        biz_alias: str = None,
        choice: int = None,
        content: str = None,
        data_source: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsDataSource = None,
        default_color: str = None,
        disabled: bool = None,
        duration: bool = None,
        duration_label: str = None,
        field_id: str = None,
        fields: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsFields] = None,
        format: str = None,
        formula: str = None,
        invisible: bool = None,
        label: str = None,
        label_editable_freeze: bool = None,
        limit: int = None,
        link: str = None,
        mode: str = None,
        multiple: bool = None,
        not_print: str = None,
        not_upper: str = None,
        options: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsOptions] = None,
        pay_enable: bool = None,
        placeholder: str = None,
        quote: int = None,
        ratio: int = None,
        relate_source: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSource] = None,
        required: bool = None,
        required_editable_freeze: bool = None,
        rule: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRule] = None,
        sortable: bool = None,
        spread: bool = None,
        stat_field: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsStatField] = None,
        table_view_mode: str = None,
        unit: str = None,
        vertical_print: bool = None,
        watermark: bool = None,
    ):
        self.action_name = action_name
        self.align = align
        self.available_templates = available_templates
        self.biz_alias = biz_alias
        self.choice = choice
        self.content = content
        self.data_source = data_source
        self.default_color = default_color
        self.disabled = disabled
        self.duration = duration
        self.duration_label = duration_label
        self.field_id = field_id
        self.fields = fields
        self.format = format
        self.formula = formula
        self.invisible = invisible
        self.label = label
        self.label_editable_freeze = label_editable_freeze
        self.limit = limit
        self.link = link
        self.mode = mode
        self.multiple = multiple
        self.not_print = not_print
        self.not_upper = not_upper
        self.options = options
        self.pay_enable = pay_enable
        self.placeholder = placeholder
        self.quote = quote
        self.ratio = ratio
        self.relate_source = relate_source
        self.required = required
        self.required_editable_freeze = required_editable_freeze
        self.rule = rule
        self.sortable = sortable
        self.spread = spread
        self.stat_field = stat_field
        self.table_view_mode = table_view_mode
        self.unit = unit
        self.vertical_print = vertical_print
        self.watermark = watermark

    def validate(self):
        if self.available_templates:
            for k in self.available_templates:
                if k:
                    k.validate()
        if self.data_source:
            self.data_source.validate()
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()
        if self.options:
            for k in self.options:
                if k:
                    k.validate()
        if self.relate_source:
            for k in self.relate_source:
                if k:
                    k.validate()
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()
        if self.stat_field:
            for k in self.stat_field:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['actionName'] = self.action_name
        if self.align is not None:
            result['align'] = self.align
        result['availableTemplates'] = []
        if self.available_templates is not None:
            for k in self.available_templates:
                result['availableTemplates'].append(k.to_map() if k else None)
        if self.biz_alias is not None:
            result['bizAlias'] = self.biz_alias
        if self.choice is not None:
            result['choice'] = self.choice
        if self.content is not None:
            result['content'] = self.content
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()
        if self.default_color is not None:
            result['defaultColor'] = self.default_color
        if self.disabled is not None:
            result['disabled'] = self.disabled
        if self.duration is not None:
            result['duration'] = self.duration
        if self.duration_label is not None:
            result['durationLabel'] = self.duration_label
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        if self.format is not None:
            result['format'] = self.format
        if self.formula is not None:
            result['formula'] = self.formula
        if self.invisible is not None:
            result['invisible'] = self.invisible
        if self.label is not None:
            result['label'] = self.label
        if self.label_editable_freeze is not None:
            result['labelEditableFreeze'] = self.label_editable_freeze
        if self.limit is not None:
            result['limit'] = self.limit
        if self.link is not None:
            result['link'] = self.link
        if self.mode is not None:
            result['mode'] = self.mode
        if self.multiple is not None:
            result['multiple'] = self.multiple
        if self.not_print is not None:
            result['notPrint'] = self.not_print
        if self.not_upper is not None:
            result['notUpper'] = self.not_upper
        result['options'] = []
        if self.options is not None:
            for k in self.options:
                result['options'].append(k.to_map() if k else None)
        if self.pay_enable is not None:
            result['payEnable'] = self.pay_enable
        if self.placeholder is not None:
            result['placeholder'] = self.placeholder
        if self.quote is not None:
            result['quote'] = self.quote
        if self.ratio is not None:
            result['ratio'] = self.ratio
        result['relateSource'] = []
        if self.relate_source is not None:
            for k in self.relate_source:
                result['relateSource'].append(k.to_map() if k else None)
        if self.required is not None:
            result['required'] = self.required
        if self.required_editable_freeze is not None:
            result['requiredEditableFreeze'] = self.required_editable_freeze
        result['rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['rule'].append(k.to_map() if k else None)
        if self.sortable is not None:
            result['sortable'] = self.sortable
        if self.spread is not None:
            result['spread'] = self.spread
        result['statField'] = []
        if self.stat_field is not None:
            for k in self.stat_field:
                result['statField'].append(k.to_map() if k else None)
        if self.table_view_mode is not None:
            result['tableViewMode'] = self.table_view_mode
        if self.unit is not None:
            result['unit'] = self.unit
        if self.vertical_print is not None:
            result['verticalPrint'] = self.vertical_print
        if self.watermark is not None:
            result['watermark'] = self.watermark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionName') is not None:
            self.action_name = m.get('actionName')
        if m.get('align') is not None:
            self.align = m.get('align')
        self.available_templates = []
        if m.get('availableTemplates') is not None:
            for k in m.get('availableTemplates'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsAvailableTemplates()
                self.available_templates.append(temp_model.from_map(k))
        if m.get('bizAlias') is not None:
            self.biz_alias = m.get('bizAlias')
        if m.get('choice') is not None:
            self.choice = m.get('choice')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dataSource') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsDataSource()
            self.data_source = temp_model.from_map(m['dataSource'])
        if m.get('defaultColor') is not None:
            self.default_color = m.get('defaultColor')
        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('durationLabel') is not None:
            self.duration_label = m.get('durationLabel')
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('formula') is not None:
            self.formula = m.get('formula')
        if m.get('invisible') is not None:
            self.invisible = m.get('invisible')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('labelEditableFreeze') is not None:
            self.label_editable_freeze = m.get('labelEditableFreeze')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('multiple') is not None:
            self.multiple = m.get('multiple')
        if m.get('notPrint') is not None:
            self.not_print = m.get('notPrint')
        if m.get('notUpper') is not None:
            self.not_upper = m.get('notUpper')
        self.options = []
        if m.get('options') is not None:
            for k in m.get('options'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsOptions()
                self.options.append(temp_model.from_map(k))
        if m.get('payEnable') is not None:
            self.pay_enable = m.get('payEnable')
        if m.get('placeholder') is not None:
            self.placeholder = m.get('placeholder')
        if m.get('quote') is not None:
            self.quote = m.get('quote')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        self.relate_source = []
        if m.get('relateSource') is not None:
            for k in m.get('relateSource'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRelateSource()
                self.relate_source.append(temp_model.from_map(k))
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('requiredEditableFreeze') is not None:
            self.required_editable_freeze = m.get('requiredEditableFreeze')
        self.rule = []
        if m.get('rule') is not None:
            for k in m.get('rule'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsRule()
                self.rule.append(temp_model.from_map(k))
        if m.get('sortable') is not None:
            self.sortable = m.get('sortable')
        if m.get('spread') is not None:
            self.spread = m.get('spread')
        self.stat_field = []
        if m.get('statField') is not None:
            for k in m.get('statField'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenPropsStatField()
                self.stat_field.append(temp_model.from_map(k))
        if m.get('tableViewMode') is not None:
            self.table_view_mode = m.get('tableViewMode')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('verticalPrint') is not None:
            self.vertical_print = m.get('verticalPrint')
        if m.get('watermark') is not None:
            self.watermark = m.get('watermark')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildren(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        props: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenProps = None,
    ):
        self.component_name = component_name
        self.props = props

    def validate(self):
        if self.props:
            self.props.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.props is not None:
            result['props'] = self.props.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('props') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildrenProps()
            self.props = temp_model.from_map(m['props'])
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsAvailableTemplates(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsDataSourceParamsFilters(TeaModel):
    def __init__(
        self,
        field_id: str = None,
        filter_type: str = None,
        value: str = None,
        value_type: str = None,
    ):
        self.field_id = field_id
        self.filter_type = filter_type
        self.value = value
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.filter_type is not None:
            result['filterType'] = self.filter_type
        if self.value is not None:
            result['value'] = self.value
        if self.value_type is not None:
            result['valueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('filterType') is not None:
            self.filter_type = m.get('filterType')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsDataSourceParams(TeaModel):
    def __init__(
        self,
        filters: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsDataSourceParamsFilters] = None,
    ):
        self.filters = filters

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['filters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('filters') is not None:
            for k in m.get('filters'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsDataSourceParamsFilters()
                self.filters.append(temp_model.from_map(k))
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsDataSourceTarget(TeaModel):
    def __init__(
        self,
        app_type: int = None,
        app_uuid: str = None,
        biz_type: str = None,
        form_code: str = None,
    ):
        self.app_type = app_type
        self.app_uuid = app_uuid
        self.biz_type = biz_type
        self.form_code = form_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.app_uuid is not None:
            result['appUuid'] = self.app_uuid
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.form_code is not None:
            result['formCode'] = self.form_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('appUuid') is not None:
            self.app_uuid = m.get('appUuid')
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('formCode') is not None:
            self.form_code = m.get('formCode')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsDataSource(TeaModel):
    def __init__(
        self,
        params: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsDataSourceParams = None,
        target: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsDataSourceTarget = None,
        type: str = None,
    ):
        self.params = params
        self.target = target
        self.type = type

    def validate(self):
        if self.params:
            self.params.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['params'] = self.params.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('params') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsDataSourceParams()
            self.params = temp_model.from_map(m['params'])
        if m.get('target') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsDataSourceTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsFieldsRelatePropsOptionsExtension(TeaModel):
    def __init__(
        self,
        edit_freeze: bool = None,
    ):
        self.edit_freeze = edit_freeze

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edit_freeze is not None:
            result['editFreeze'] = self.edit_freeze
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('editFreeze') is not None:
            self.edit_freeze = m.get('editFreeze')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsFieldsRelatePropsOptions(TeaModel):
    def __init__(
        self,
        extension: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsFieldsRelatePropsOptionsExtension = None,
        key: str = None,
        value: str = None,
    ):
        self.extension = extension
        self.key = key
        self.value = value

    def validate(self):
        if self.extension:
            self.extension.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['extension'] = self.extension.to_map()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extension') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsFieldsRelatePropsOptionsExtension()
            self.extension = temp_model.from_map(m['extension'])
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsFieldsRelatePropsStatField(TeaModel):
    def __init__(
        self,
        field_id: str = None,
        label: str = None,
        unit: str = None,
        upper: bool = None,
    ):
        self.field_id = field_id
        self.label = label
        self.unit = unit
        self.upper = upper

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.label is not None:
            result['label'] = self.label
        if self.unit is not None:
            result['unit'] = self.unit
        if self.upper is not None:
            result['upper'] = self.upper
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('upper') is not None:
            self.upper = m.get('upper')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsFieldsRelateProps(TeaModel):
    def __init__(
        self,
        align: str = None,
        biz_alias: str = None,
        choice: int = None,
        content: str = None,
        disabled: bool = None,
        duration: str = None,
        duration_label: str = None,
        field_id: str = None,
        format: str = None,
        formula: str = None,
        invisible: bool = None,
        label: str = None,
        label_editable_freeze: bool = None,
        limit: int = None,
        link: str = None,
        mode: str = None,
        not_upper: str = None,
        options: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsFieldsRelatePropsOptions] = None,
        pay_enable: bool = None,
        placeholder: str = None,
        ratio: int = None,
        required: bool = None,
        required_editable_freeze: bool = None,
        spread: bool = None,
        stat_field: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsFieldsRelatePropsStatField] = None,
        unit: str = None,
        vertical_print: bool = None,
        watermark: bool = None,
    ):
        self.align = align
        self.biz_alias = biz_alias
        self.choice = choice
        self.content = content
        self.disabled = disabled
        self.duration = duration
        self.duration_label = duration_label
        self.field_id = field_id
        self.format = format
        self.formula = formula
        self.invisible = invisible
        self.label = label
        self.label_editable_freeze = label_editable_freeze
        self.limit = limit
        self.link = link
        self.mode = mode
        self.not_upper = not_upper
        self.options = options
        self.pay_enable = pay_enable
        self.placeholder = placeholder
        self.ratio = ratio
        self.required = required
        self.required_editable_freeze = required_editable_freeze
        self.spread = spread
        self.stat_field = stat_field
        self.unit = unit
        self.vertical_print = vertical_print
        self.watermark = watermark

    def validate(self):
        if self.options:
            for k in self.options:
                if k:
                    k.validate()
        if self.stat_field:
            for k in self.stat_field:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align is not None:
            result['align'] = self.align
        if self.biz_alias is not None:
            result['bizAlias'] = self.biz_alias
        if self.choice is not None:
            result['choice'] = self.choice
        if self.content is not None:
            result['content'] = self.content
        if self.disabled is not None:
            result['disabled'] = self.disabled
        if self.duration is not None:
            result['duration'] = self.duration
        if self.duration_label is not None:
            result['durationLabel'] = self.duration_label
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.format is not None:
            result['format'] = self.format
        if self.formula is not None:
            result['formula'] = self.formula
        if self.invisible is not None:
            result['invisible'] = self.invisible
        if self.label is not None:
            result['label'] = self.label
        if self.label_editable_freeze is not None:
            result['labelEditableFreeze'] = self.label_editable_freeze
        if self.limit is not None:
            result['limit'] = self.limit
        if self.link is not None:
            result['link'] = self.link
        if self.mode is not None:
            result['mode'] = self.mode
        if self.not_upper is not None:
            result['notUpper'] = self.not_upper
        result['options'] = []
        if self.options is not None:
            for k in self.options:
                result['options'].append(k.to_map() if k else None)
        if self.pay_enable is not None:
            result['payEnable'] = self.pay_enable
        if self.placeholder is not None:
            result['placeholder'] = self.placeholder
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.required is not None:
            result['required'] = self.required
        if self.required_editable_freeze is not None:
            result['requiredEditableFreeze'] = self.required_editable_freeze
        if self.spread is not None:
            result['spread'] = self.spread
        result['statField'] = []
        if self.stat_field is not None:
            for k in self.stat_field:
                result['statField'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['unit'] = self.unit
        if self.vertical_print is not None:
            result['verticalPrint'] = self.vertical_print
        if self.watermark is not None:
            result['watermark'] = self.watermark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('align') is not None:
            self.align = m.get('align')
        if m.get('bizAlias') is not None:
            self.biz_alias = m.get('bizAlias')
        if m.get('choice') is not None:
            self.choice = m.get('choice')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('durationLabel') is not None:
            self.duration_label = m.get('durationLabel')
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('formula') is not None:
            self.formula = m.get('formula')
        if m.get('invisible') is not None:
            self.invisible = m.get('invisible')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('labelEditableFreeze') is not None:
            self.label_editable_freeze = m.get('labelEditableFreeze')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('notUpper') is not None:
            self.not_upper = m.get('notUpper')
        self.options = []
        if m.get('options') is not None:
            for k in m.get('options'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsFieldsRelatePropsOptions()
                self.options.append(temp_model.from_map(k))
        if m.get('payEnable') is not None:
            self.pay_enable = m.get('payEnable')
        if m.get('placeholder') is not None:
            self.placeholder = m.get('placeholder')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('requiredEditableFreeze') is not None:
            self.required_editable_freeze = m.get('requiredEditableFreeze')
        if m.get('spread') is not None:
            self.spread = m.get('spread')
        self.stat_field = []
        if m.get('statField') is not None:
            for k in m.get('statField'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsFieldsRelatePropsStatField()
                self.stat_field.append(temp_model.from_map(k))
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('verticalPrint') is not None:
            self.vertical_print = m.get('verticalPrint')
        if m.get('watermark') is not None:
            self.watermark = m.get('watermark')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsFields(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        relate_props: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsFieldsRelateProps = None,
    ):
        self.component_name = component_name
        self.relate_props = relate_props

    def validate(self):
        if self.relate_props:
            self.relate_props.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.relate_props is not None:
            result['relateProps'] = self.relate_props.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('relateProps') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsFieldsRelateProps()
            self.relate_props = temp_model.from_map(m['relateProps'])
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsOptionsExtension(TeaModel):
    def __init__(
        self,
        edit_freeze: bool = None,
    ):
        self.edit_freeze = edit_freeze

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edit_freeze is not None:
            result['editFreeze'] = self.edit_freeze
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('editFreeze') is not None:
            self.edit_freeze = m.get('editFreeze')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsOptions(TeaModel):
    def __init__(
        self,
        extension: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsOptionsExtension = None,
        key: str = None,
        value: str = None,
        warn: bool = None,
    ):
        self.extension = extension
        self.key = key
        self.value = value
        self.warn = warn

    def validate(self):
        if self.extension:
            self.extension.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['extension'] = self.extension.to_map()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        if self.warn is not None:
            result['warn'] = self.warn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extension') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsOptionsExtension()
            self.extension = temp_model.from_map(m['extension'])
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('warn') is not None:
            self.warn = m.get('warn')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceDataSourceParamsFilters(TeaModel):
    def __init__(
        self,
        field_id: str = None,
        filter_type: str = None,
        value: str = None,
        value_type: str = None,
    ):
        self.field_id = field_id
        self.filter_type = filter_type
        self.value = value
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.filter_type is not None:
            result['filterType'] = self.filter_type
        if self.value is not None:
            result['value'] = self.value
        if self.value_type is not None:
            result['valueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('filterType') is not None:
            self.filter_type = m.get('filterType')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceDataSourceParams(TeaModel):
    def __init__(
        self,
        filters: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceDataSourceParamsFilters] = None,
    ):
        self.filters = filters

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['filters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('filters') is not None:
            for k in m.get('filters'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceDataSourceParamsFilters()
                self.filters.append(temp_model.from_map(k))
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceDataSourceTarget(TeaModel):
    def __init__(
        self,
        app_type: int = None,
        app_uuid: str = None,
        biz_type: str = None,
        form_code: str = None,
    ):
        self.app_type = app_type
        self.app_uuid = app_uuid
        self.biz_type = biz_type
        self.form_code = form_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.app_uuid is not None:
            result['appUuid'] = self.app_uuid
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.form_code is not None:
            result['formCode'] = self.form_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('appUuid') is not None:
            self.app_uuid = m.get('appUuid')
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('formCode') is not None:
            self.form_code = m.get('formCode')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceDataSource(TeaModel):
    def __init__(
        self,
        params: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceDataSourceParams = None,
        target: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceDataSourceTarget = None,
        type: str = None,
    ):
        self.params = params
        self.target = target
        self.type = type

    def validate(self):
        if self.params:
            self.params.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['params'] = self.params.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('params') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceDataSourceParams()
            self.params = temp_model.from_map(m['params'])
        if m.get('target') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceDataSourceTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceFieldsRelatePropsOptionsExtension(TeaModel):
    def __init__(
        self,
        edit_freeze: bool = None,
    ):
        self.edit_freeze = edit_freeze

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edit_freeze is not None:
            result['editFreeze'] = self.edit_freeze
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('editFreeze') is not None:
            self.edit_freeze = m.get('editFreeze')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceFieldsRelatePropsOptions(TeaModel):
    def __init__(
        self,
        extension: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceFieldsRelatePropsOptionsExtension = None,
        key: str = None,
        value: str = None,
    ):
        self.extension = extension
        self.key = key
        self.value = value

    def validate(self):
        if self.extension:
            self.extension.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['extension'] = self.extension.to_map()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extension') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceFieldsRelatePropsOptionsExtension()
            self.extension = temp_model.from_map(m['extension'])
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceFieldsRelatePropsStatField(TeaModel):
    def __init__(
        self,
        field_id: str = None,
        label: str = None,
        unit: str = None,
        upper: bool = None,
    ):
        self.field_id = field_id
        self.label = label
        self.unit = unit
        self.upper = upper

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.label is not None:
            result['label'] = self.label
        if self.unit is not None:
            result['unit'] = self.unit
        if self.upper is not None:
            result['upper'] = self.upper
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('upper') is not None:
            self.upper = m.get('upper')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceFieldsRelateProps(TeaModel):
    def __init__(
        self,
        align: str = None,
        biz_alias: str = None,
        choice: int = None,
        content: str = None,
        disabled: bool = None,
        duration: str = None,
        field_id: str = None,
        format: str = None,
        formula: str = None,
        invisible: bool = None,
        label: str = None,
        label_editable_freeze: bool = None,
        link: str = None,
        multi: int = None,
        not_upper: str = None,
        options: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceFieldsRelatePropsOptions] = None,
        pay_enable: bool = None,
        placeholder: str = None,
        quote: int = None,
        required: bool = None,
        required_editable_freeze: bool = None,
        stat_field: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceFieldsRelatePropsStatField] = None,
        unit: str = None,
        vertical_print: bool = None,
    ):
        self.align = align
        self.biz_alias = biz_alias
        self.choice = choice
        self.content = content
        self.disabled = disabled
        self.duration = duration
        self.field_id = field_id
        self.format = format
        self.formula = formula
        self.invisible = invisible
        self.label = label
        self.label_editable_freeze = label_editable_freeze
        self.link = link
        self.multi = multi
        self.not_upper = not_upper
        self.options = options
        self.pay_enable = pay_enable
        self.placeholder = placeholder
        self.quote = quote
        self.required = required
        self.required_editable_freeze = required_editable_freeze
        self.stat_field = stat_field
        self.unit = unit
        self.vertical_print = vertical_print

    def validate(self):
        if self.options:
            for k in self.options:
                if k:
                    k.validate()
        if self.stat_field:
            for k in self.stat_field:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align is not None:
            result['align'] = self.align
        if self.biz_alias is not None:
            result['bizAlias'] = self.biz_alias
        if self.choice is not None:
            result['choice'] = self.choice
        if self.content is not None:
            result['content'] = self.content
        if self.disabled is not None:
            result['disabled'] = self.disabled
        if self.duration is not None:
            result['duration'] = self.duration
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.format is not None:
            result['format'] = self.format
        if self.formula is not None:
            result['formula'] = self.formula
        if self.invisible is not None:
            result['invisible'] = self.invisible
        if self.label is not None:
            result['label'] = self.label
        if self.label_editable_freeze is not None:
            result['labelEditableFreeze'] = self.label_editable_freeze
        if self.link is not None:
            result['link'] = self.link
        if self.multi is not None:
            result['multi'] = self.multi
        if self.not_upper is not None:
            result['notUpper'] = self.not_upper
        result['options'] = []
        if self.options is not None:
            for k in self.options:
                result['options'].append(k.to_map() if k else None)
        if self.pay_enable is not None:
            result['payEnable'] = self.pay_enable
        if self.placeholder is not None:
            result['placeholder'] = self.placeholder
        if self.quote is not None:
            result['quote'] = self.quote
        if self.required is not None:
            result['required'] = self.required
        if self.required_editable_freeze is not None:
            result['requiredEditableFreeze'] = self.required_editable_freeze
        result['statField'] = []
        if self.stat_field is not None:
            for k in self.stat_field:
                result['statField'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['unit'] = self.unit
        if self.vertical_print is not None:
            result['verticalPrint'] = self.vertical_print
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('align') is not None:
            self.align = m.get('align')
        if m.get('bizAlias') is not None:
            self.biz_alias = m.get('bizAlias')
        if m.get('choice') is not None:
            self.choice = m.get('choice')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('formula') is not None:
            self.formula = m.get('formula')
        if m.get('invisible') is not None:
            self.invisible = m.get('invisible')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('labelEditableFreeze') is not None:
            self.label_editable_freeze = m.get('labelEditableFreeze')
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('multi') is not None:
            self.multi = m.get('multi')
        if m.get('notUpper') is not None:
            self.not_upper = m.get('notUpper')
        self.options = []
        if m.get('options') is not None:
            for k in m.get('options'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceFieldsRelatePropsOptions()
                self.options.append(temp_model.from_map(k))
        if m.get('payEnable') is not None:
            self.pay_enable = m.get('payEnable')
        if m.get('placeholder') is not None:
            self.placeholder = m.get('placeholder')
        if m.get('quote') is not None:
            self.quote = m.get('quote')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('requiredEditableFreeze') is not None:
            self.required_editable_freeze = m.get('requiredEditableFreeze')
        self.stat_field = []
        if m.get('statField') is not None:
            for k in m.get('statField'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceFieldsRelatePropsStatField()
                self.stat_field.append(temp_model.from_map(k))
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('verticalPrint') is not None:
            self.vertical_print = m.get('verticalPrint')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceFields(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        relate_props: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceFieldsRelateProps = None,
    ):
        self.component_name = component_name
        self.relate_props = relate_props

    def validate(self):
        if self.relate_props:
            self.relate_props.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.relate_props is not None:
            result['relateProps'] = self.relate_props.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('relateProps') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceFieldsRelateProps()
            self.relate_props = temp_model.from_map(m['relateProps'])
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSource(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        data_source: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceDataSource = None,
        fields: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceFields] = None,
    ):
        self.biz_type = biz_type
        self.data_source = data_source
        self.fields = fields

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('dataSource') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceDataSource()
            self.data_source = temp_model.from_map(m['dataSource'])
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSourceFields()
                self.fields.append(temp_model.from_map(k))
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRule(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsStatField(TeaModel):
    def __init__(
        self,
        field_id: str = None,
        label: str = None,
        unit: str = None,
        upper: bool = None,
    ):
        self.field_id = field_id
        self.label = label
        self.unit = unit
        self.upper = upper

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.label is not None:
            result['label'] = self.label
        if self.unit is not None:
            result['unit'] = self.unit
        if self.upper is not None:
            result['upper'] = self.upper
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('upper') is not None:
            self.upper = m.get('upper')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItemsProps(TeaModel):
    def __init__(
        self,
        action_name: str = None,
        align: str = None,
        available_templates: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsAvailableTemplates] = None,
        biz_alias: str = None,
        choice: int = None,
        content: str = None,
        data_source: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsDataSource = None,
        default_color: str = None,
        disabled: bool = None,
        duration: bool = None,
        duration_label: str = None,
        field_id: str = None,
        fields: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsFields] = None,
        format: str = None,
        formula: str = None,
        invisible: bool = None,
        label: str = None,
        label_editable_freeze: bool = None,
        limit: int = None,
        link: str = None,
        mode: str = None,
        multi: int = None,
        multiple: bool = None,
        need_detail: str = None,
        not_print: str = None,
        not_upper: str = None,
        options: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsOptions] = None,
        pay_enable: bool = None,
        placeholder: str = None,
        quote: int = None,
        ratio: int = None,
        relate_source: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSource] = None,
        required: bool = None,
        required_editable_freeze: bool = None,
        rule: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRule] = None,
        sortable: bool = None,
        spread: bool = None,
        stat_field: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsStatField] = None,
        table_view_mode: str = None,
        unit: str = None,
        vertical_print: bool = None,
        watermark: bool = None,
    ):
        self.action_name = action_name
        self.align = align
        self.available_templates = available_templates
        self.biz_alias = biz_alias
        self.choice = choice
        self.content = content
        self.data_source = data_source
        self.default_color = default_color
        self.disabled = disabled
        self.duration = duration
        self.duration_label = duration_label
        self.field_id = field_id
        self.fields = fields
        self.format = format
        self.formula = formula
        self.invisible = invisible
        self.label = label
        self.label_editable_freeze = label_editable_freeze
        self.limit = limit
        self.link = link
        self.mode = mode
        self.multi = multi
        self.multiple = multiple
        self.need_detail = need_detail
        self.not_print = not_print
        self.not_upper = not_upper
        self.options = options
        self.pay_enable = pay_enable
        self.placeholder = placeholder
        self.quote = quote
        self.ratio = ratio
        self.relate_source = relate_source
        self.required = required
        self.required_editable_freeze = required_editable_freeze
        self.rule = rule
        self.sortable = sortable
        self.spread = spread
        self.stat_field = stat_field
        self.table_view_mode = table_view_mode
        self.unit = unit
        self.vertical_print = vertical_print
        self.watermark = watermark

    def validate(self):
        if self.available_templates:
            for k in self.available_templates:
                if k:
                    k.validate()
        if self.data_source:
            self.data_source.validate()
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()
        if self.options:
            for k in self.options:
                if k:
                    k.validate()
        if self.relate_source:
            for k in self.relate_source:
                if k:
                    k.validate()
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()
        if self.stat_field:
            for k in self.stat_field:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['actionName'] = self.action_name
        if self.align is not None:
            result['align'] = self.align
        result['availableTemplates'] = []
        if self.available_templates is not None:
            for k in self.available_templates:
                result['availableTemplates'].append(k.to_map() if k else None)
        if self.biz_alias is not None:
            result['bizAlias'] = self.biz_alias
        if self.choice is not None:
            result['choice'] = self.choice
        if self.content is not None:
            result['content'] = self.content
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()
        if self.default_color is not None:
            result['defaultColor'] = self.default_color
        if self.disabled is not None:
            result['disabled'] = self.disabled
        if self.duration is not None:
            result['duration'] = self.duration
        if self.duration_label is not None:
            result['durationLabel'] = self.duration_label
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        if self.format is not None:
            result['format'] = self.format
        if self.formula is not None:
            result['formula'] = self.formula
        if self.invisible is not None:
            result['invisible'] = self.invisible
        if self.label is not None:
            result['label'] = self.label
        if self.label_editable_freeze is not None:
            result['labelEditableFreeze'] = self.label_editable_freeze
        if self.limit is not None:
            result['limit'] = self.limit
        if self.link is not None:
            result['link'] = self.link
        if self.mode is not None:
            result['mode'] = self.mode
        if self.multi is not None:
            result['multi'] = self.multi
        if self.multiple is not None:
            result['multiple'] = self.multiple
        if self.need_detail is not None:
            result['needDetail'] = self.need_detail
        if self.not_print is not None:
            result['notPrint'] = self.not_print
        if self.not_upper is not None:
            result['notUpper'] = self.not_upper
        result['options'] = []
        if self.options is not None:
            for k in self.options:
                result['options'].append(k.to_map() if k else None)
        if self.pay_enable is not None:
            result['payEnable'] = self.pay_enable
        if self.placeholder is not None:
            result['placeholder'] = self.placeholder
        if self.quote is not None:
            result['quote'] = self.quote
        if self.ratio is not None:
            result['ratio'] = self.ratio
        result['relateSource'] = []
        if self.relate_source is not None:
            for k in self.relate_source:
                result['relateSource'].append(k.to_map() if k else None)
        if self.required is not None:
            result['required'] = self.required
        if self.required_editable_freeze is not None:
            result['requiredEditableFreeze'] = self.required_editable_freeze
        result['rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['rule'].append(k.to_map() if k else None)
        if self.sortable is not None:
            result['sortable'] = self.sortable
        if self.spread is not None:
            result['spread'] = self.spread
        result['statField'] = []
        if self.stat_field is not None:
            for k in self.stat_field:
                result['statField'].append(k.to_map() if k else None)
        if self.table_view_mode is not None:
            result['tableViewMode'] = self.table_view_mode
        if self.unit is not None:
            result['unit'] = self.unit
        if self.vertical_print is not None:
            result['verticalPrint'] = self.vertical_print
        if self.watermark is not None:
            result['watermark'] = self.watermark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionName') is not None:
            self.action_name = m.get('actionName')
        if m.get('align') is not None:
            self.align = m.get('align')
        self.available_templates = []
        if m.get('availableTemplates') is not None:
            for k in m.get('availableTemplates'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsAvailableTemplates()
                self.available_templates.append(temp_model.from_map(k))
        if m.get('bizAlias') is not None:
            self.biz_alias = m.get('bizAlias')
        if m.get('choice') is not None:
            self.choice = m.get('choice')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dataSource') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsDataSource()
            self.data_source = temp_model.from_map(m['dataSource'])
        if m.get('defaultColor') is not None:
            self.default_color = m.get('defaultColor')
        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('durationLabel') is not None:
            self.duration_label = m.get('durationLabel')
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('formula') is not None:
            self.formula = m.get('formula')
        if m.get('invisible') is not None:
            self.invisible = m.get('invisible')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('labelEditableFreeze') is not None:
            self.label_editable_freeze = m.get('labelEditableFreeze')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('multi') is not None:
            self.multi = m.get('multi')
        if m.get('multiple') is not None:
            self.multiple = m.get('multiple')
        if m.get('needDetail') is not None:
            self.need_detail = m.get('needDetail')
        if m.get('notPrint') is not None:
            self.not_print = m.get('notPrint')
        if m.get('notUpper') is not None:
            self.not_upper = m.get('notUpper')
        self.options = []
        if m.get('options') is not None:
            for k in m.get('options'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsOptions()
                self.options.append(temp_model.from_map(k))
        if m.get('payEnable') is not None:
            self.pay_enable = m.get('payEnable')
        if m.get('placeholder') is not None:
            self.placeholder = m.get('placeholder')
        if m.get('quote') is not None:
            self.quote = m.get('quote')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        self.relate_source = []
        if m.get('relateSource') is not None:
            for k in m.get('relateSource'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRelateSource()
                self.relate_source.append(temp_model.from_map(k))
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('requiredEditableFreeze') is not None:
            self.required_editable_freeze = m.get('requiredEditableFreeze')
        self.rule = []
        if m.get('rule') is not None:
            for k in m.get('rule'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsRule()
                self.rule.append(temp_model.from_map(k))
        if m.get('sortable') is not None:
            self.sortable = m.get('sortable')
        if m.get('spread') is not None:
            self.spread = m.get('spread')
        self.stat_field = []
        if m.get('statField') is not None:
            for k in m.get('statField'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsPropsStatField()
                self.stat_field.append(temp_model.from_map(k))
        if m.get('tableViewMode') is not None:
            self.table_view_mode = m.get('tableViewMode')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('verticalPrint') is not None:
            self.vertical_print = m.get('verticalPrint')
        if m.get('watermark') is not None:
            self.watermark = m.get('watermark')
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOListItems(TeaModel):
    def __init__(
        self,
        children: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildren] = None,
        component_name: str = None,
        props: DescribeRelationMetaResponseBodyRelationMetaDTOListItemsProps = None,
    ):
        self.children = children
        self.component_name = component_name
        self.props = props

    def validate(self):
        if self.children:
            for k in self.children:
                if k:
                    k.validate()
        if self.props:
            self.props.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['children'] = []
        if self.children is not None:
            for k in self.children:
                result['children'].append(k.to_map() if k else None)
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.props is not None:
            result['props'] = self.props.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('children') is not None:
            for k in m.get('children'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsChildren()
                self.children.append(temp_model.from_map(k))
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('props') is not None:
            temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItemsProps()
            self.props = temp_model.from_map(m['props'])
        return self


class DescribeRelationMetaResponseBodyRelationMetaDTOList(TeaModel):
    def __init__(
        self,
        creator_user_id: str = None,
        desc: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        items: List[DescribeRelationMetaResponseBodyRelationMetaDTOListItems] = None,
        name: str = None,
        relation_meta_code: str = None,
        relation_meta_status: str = None,
        relation_type: str = None,
    ):
        self.creator_user_id = creator_user_id
        self.desc = desc
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.items = items
        self.name = name
        self.relation_meta_code = relation_meta_code
        self.relation_meta_status = relation_meta_status
        self.relation_type = relation_type

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_user_id is not None:
            result['creatorUserId'] = self.creator_user_id
        if self.desc is not None:
            result['desc'] = self.desc
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.relation_meta_code is not None:
            result['relationMetaCode'] = self.relation_meta_code
        if self.relation_meta_status is not None:
            result['relationMetaStatus'] = self.relation_meta_status
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorUserId') is not None:
            self.creator_user_id = m.get('creatorUserId')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('relationMetaCode') is not None:
            self.relation_meta_code = m.get('relationMetaCode')
        if m.get('relationMetaStatus') is not None:
            self.relation_meta_status = m.get('relationMetaStatus')
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        return self


class DescribeRelationMetaResponseBody(TeaModel):
    def __init__(
        self,
        relation_meta_dtolist: List[DescribeRelationMetaResponseBodyRelationMetaDTOList] = None,
    ):
        self.relation_meta_dtolist = relation_meta_dtolist

    def validate(self):
        if self.relation_meta_dtolist:
            for k in self.relation_meta_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['relationMetaDTOList'] = []
        if self.relation_meta_dtolist is not None:
            for k in self.relation_meta_dtolist:
                result['relationMetaDTOList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.relation_meta_dtolist = []
        if m.get('relationMetaDTOList') is not None:
            for k in m.get('relationMetaDTOList'):
                temp_model = DescribeRelationMetaResponseBodyRelationMetaDTOList()
                self.relation_meta_dtolist.append(temp_model.from_map(k))
        return self


class DescribeRelationMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRelationMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRelationMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAllCustomerRecyclesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetAllCustomerRecyclesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class GetAllCustomerRecyclesResponseBodyResultList(TeaModel):
    def __init__(
        self,
        customer_id: str = None,
        follow_up_action_time: str = None,
        is_deleted: bool = None,
        notify_time: str = None,
        recycle_rule_id: int = None,
        recycle_time: str = None,
    ):
        self.customer_id = customer_id
        self.follow_up_action_time = follow_up_action_time
        self.is_deleted = is_deleted
        self.notify_time = notify_time
        self.recycle_rule_id = recycle_rule_id
        self.recycle_time = recycle_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.follow_up_action_time is not None:
            result['followUpActionTime'] = self.follow_up_action_time
        if self.is_deleted is not None:
            result['isDeleted'] = self.is_deleted
        if self.notify_time is not None:
            result['notifyTime'] = self.notify_time
        if self.recycle_rule_id is not None:
            result['recycleRuleId'] = self.recycle_rule_id
        if self.recycle_time is not None:
            result['recycleTime'] = self.recycle_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('followUpActionTime') is not None:
            self.follow_up_action_time = m.get('followUpActionTime')
        if m.get('isDeleted') is not None:
            self.is_deleted = m.get('isDeleted')
        if m.get('notifyTime') is not None:
            self.notify_time = m.get('notifyTime')
        if m.get('recycleRuleId') is not None:
            self.recycle_rule_id = m.get('recycleRuleId')
        if m.get('recycleTime') is not None:
            self.recycle_time = m.get('recycleTime')
        return self


class GetAllCustomerRecyclesResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        next_token: str = None,
        result_list: List[GetAllCustomerRecyclesResponseBodyResultList] = None,
    ):
        self.has_more = has_more
        self.next_token = next_token
        self.result_list = result_list

    def validate(self):
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['resultList'] = []
        if self.result_list is not None:
            for k in self.result_list:
                result['resultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.result_list = []
        if m.get('resultList') is not None:
            for k in m.get('resultList'):
                temp_model = GetAllCustomerRecyclesResponseBodyResultList()
                self.result_list.append(temp_model.from_map(k))
        return self


class GetAllCustomerRecyclesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAllCustomerRecyclesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAllCustomerRecyclesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCrmGroupChatHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetCrmGroupChatResponseBody(TeaModel):
    def __init__(
        self,
        chat_id: str = None,
        gmt_create: int = None,
        icon_url: str = None,
        member_count: int = None,
        name: str = None,
        open_conversation_id: str = None,
        open_group_set_id: str = None,
        owner_user_id: str = None,
        owner_user_name: str = None,
    ):
        self.chat_id = chat_id
        self.gmt_create = gmt_create
        self.icon_url = icon_url
        self.member_count = member_count
        self.name = name
        self.open_conversation_id = open_conversation_id
        self.open_group_set_id = open_group_set_id
        self.owner_user_id = owner_user_id
        self.owner_user_name = owner_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.icon_url is not None:
            result['iconUrl'] = self.icon_url
        if self.member_count is not None:
            result['memberCount'] = self.member_count
        if self.name is not None:
            result['name'] = self.name
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.owner_user_id is not None:
            result['ownerUserId'] = self.owner_user_id
        if self.owner_user_name is not None:
            result['ownerUserName'] = self.owner_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('iconUrl') is not None:
            self.icon_url = m.get('iconUrl')
        if m.get('memberCount') is not None:
            self.member_count = m.get('memberCount')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('ownerUserId') is not None:
            self.owner_user_id = m.get('ownerUserId')
        if m.get('ownerUserName') is not None:
            self.owner_user_name = m.get('ownerUserName')
        return self


class GetCrmGroupChatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCrmGroupChatResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCrmGroupChatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCrmGroupChatMultiHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetCrmGroupChatMultiRequest(TeaModel):
    def __init__(
        self,
        open_conversation_ids: List[str] = None,
    ):
        self.open_conversation_ids = open_conversation_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_conversation_ids is not None:
            result['openConversationIds'] = self.open_conversation_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openConversationIds') is not None:
            self.open_conversation_ids = m.get('openConversationIds')
        return self


class GetCrmGroupChatMultiResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        icon_url: str = None,
        member_count: int = None,
        name: str = None,
        open_conversation_id: str = None,
        open_group_set_id: str = None,
        owner_user_id: str = None,
        owner_user_name: str = None,
    ):
        self.gmt_create = gmt_create
        self.icon_url = icon_url
        self.member_count = member_count
        self.name = name
        self.open_conversation_id = open_conversation_id
        self.open_group_set_id = open_group_set_id
        self.owner_user_id = owner_user_id
        self.owner_user_name = owner_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.icon_url is not None:
            result['iconUrl'] = self.icon_url
        if self.member_count is not None:
            result['memberCount'] = self.member_count
        if self.name is not None:
            result['name'] = self.name
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.owner_user_id is not None:
            result['ownerUserId'] = self.owner_user_id
        if self.owner_user_name is not None:
            result['ownerUserName'] = self.owner_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('iconUrl') is not None:
            self.icon_url = m.get('iconUrl')
        if m.get('memberCount') is not None:
            self.member_count = m.get('memberCount')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('ownerUserId') is not None:
            self.owner_user_id = m.get('ownerUserId')
        if m.get('ownerUserName') is not None:
            self.owner_user_name = m.get('ownerUserName')
        return self


class GetCrmGroupChatMultiResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetCrmGroupChatMultiResponseBodyResult] = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = GetCrmGroupChatMultiResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetCrmGroupChatMultiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCrmGroupChatMultiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCrmGroupChatMultiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCrmGroupChatSingleHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetCrmGroupChatSingleRequest(TeaModel):
    def __init__(
        self,
        open_conversation_id: str = None,
    ):
        self.open_conversation_id = open_conversation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        return self


class GetCrmGroupChatSingleResponseBody(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        icon_url: str = None,
        member_count: int = None,
        name: str = None,
        open_conversation_id: str = None,
        open_group_set_id: str = None,
        owner_user_id: str = None,
        owner_user_name: str = None,
    ):
        self.gmt_create = gmt_create
        self.icon_url = icon_url
        self.member_count = member_count
        self.name = name
        self.open_conversation_id = open_conversation_id
        self.open_group_set_id = open_group_set_id
        self.owner_user_id = owner_user_id
        self.owner_user_name = owner_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.icon_url is not None:
            result['iconUrl'] = self.icon_url
        if self.member_count is not None:
            result['memberCount'] = self.member_count
        if self.name is not None:
            result['name'] = self.name
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.owner_user_id is not None:
            result['ownerUserId'] = self.owner_user_id
        if self.owner_user_name is not None:
            result['ownerUserName'] = self.owner_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('iconUrl') is not None:
            self.icon_url = m.get('iconUrl')
        if m.get('memberCount') is not None:
            self.member_count = m.get('memberCount')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('ownerUserId') is not None:
            self.owner_user_id = m.get('ownerUserId')
        if m.get('ownerUserName') is not None:
            self.owner_user_name = m.get('ownerUserName')
        return self


class GetCrmGroupChatSingleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCrmGroupChatSingleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCrmGroupChatSingleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCrmRolePermissionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetCrmRolePermissionRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        resource_id: str = None,
    ):
        self.biz_type = biz_type
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        return self


class GetCrmRolePermissionResponseBodyPermissionsFieldScopes(TeaModel):
    def __init__(
        self,
        field_actions: List[str] = None,
        field_id: str = None,
    ):
        self.field_actions = field_actions
        self.field_id = field_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_actions is not None:
            result['fieldActions'] = self.field_actions
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldActions') is not None:
            self.field_actions = m.get('fieldActions')
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        return self


class GetCrmRolePermissionResponseBodyPermissionsManagingScopeListExt(TeaModel):
    def __init__(
        self,
        dept_id_list: List[float] = None,
        user_id_list: List[str] = None,
    ):
        self.dept_id_list = dept_id_list
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_id_list is not None:
            result['deptIdList'] = self.dept_id_list
        if self.user_id_list is not None:
            result['userIdList'] = self.user_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptIdList') is not None:
            self.dept_id_list = m.get('deptIdList')
        if m.get('userIdList') is not None:
            self.user_id_list = m.get('userIdList')
        return self


class GetCrmRolePermissionResponseBodyPermissionsManagingScopeList(TeaModel):
    def __init__(
        self,
        ext: GetCrmRolePermissionResponseBodyPermissionsManagingScopeListExt = None,
        manager: bool = None,
        type: str = None,
    ):
        self.ext = ext
        self.manager = manager
        self.type = type

    def validate(self):
        if self.ext:
            self.ext.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['ext'] = self.ext.to_map()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ext') is not None:
            temp_model = GetCrmRolePermissionResponseBodyPermissionsManagingScopeListExt()
            self.ext = temp_model.from_map(m['ext'])
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetCrmRolePermissionResponseBodyPermissionsOperateScopes(TeaModel):
    def __init__(
        self,
        has_auth: bool = None,
        type: str = None,
    ):
        self.has_auth = has_auth
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_auth is not None:
            result['hasAuth'] = self.has_auth
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasAuth') is not None:
            self.has_auth = m.get('hasAuth')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetCrmRolePermissionResponseBodyPermissionsRoleMemberList(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        name: str = None,
        type: str = None,
        user_id: str = None,
    ):
        self.member_id = member_id
        self.name = name
        self.type = type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['memberId'] = self.member_id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memberId') is not None:
            self.member_id = m.get('memberId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetCrmRolePermissionResponseBodyPermissions(TeaModel):
    def __init__(
        self,
        default_role: bool = None,
        field_scopes: List[GetCrmRolePermissionResponseBodyPermissionsFieldScopes] = None,
        managing_scope_list: List[GetCrmRolePermissionResponseBodyPermissionsManagingScopeList] = None,
        operate_scopes: List[GetCrmRolePermissionResponseBodyPermissionsOperateScopes] = None,
        resource_id: str = None,
        role_id: float = None,
        role_member_list: List[GetCrmRolePermissionResponseBodyPermissionsRoleMemberList] = None,
        role_name: str = None,
    ):
        self.default_role = default_role
        self.field_scopes = field_scopes
        self.managing_scope_list = managing_scope_list
        self.operate_scopes = operate_scopes
        self.resource_id = resource_id
        self.role_id = role_id
        self.role_member_list = role_member_list
        self.role_name = role_name

    def validate(self):
        if self.field_scopes:
            for k in self.field_scopes:
                if k:
                    k.validate()
        if self.managing_scope_list:
            for k in self.managing_scope_list:
                if k:
                    k.validate()
        if self.operate_scopes:
            for k in self.operate_scopes:
                if k:
                    k.validate()
        if self.role_member_list:
            for k in self.role_member_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_role is not None:
            result['defaultRole'] = self.default_role
        result['fieldScopes'] = []
        if self.field_scopes is not None:
            for k in self.field_scopes:
                result['fieldScopes'].append(k.to_map() if k else None)
        result['managingScopeList'] = []
        if self.managing_scope_list is not None:
            for k in self.managing_scope_list:
                result['managingScopeList'].append(k.to_map() if k else None)
        result['operateScopes'] = []
        if self.operate_scopes is not None:
            for k in self.operate_scopes:
                result['operateScopes'].append(k.to_map() if k else None)
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.role_id is not None:
            result['roleId'] = self.role_id
        result['roleMemberList'] = []
        if self.role_member_list is not None:
            for k in self.role_member_list:
                result['roleMemberList'].append(k.to_map() if k else None)
        if self.role_name is not None:
            result['roleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultRole') is not None:
            self.default_role = m.get('defaultRole')
        self.field_scopes = []
        if m.get('fieldScopes') is not None:
            for k in m.get('fieldScopes'):
                temp_model = GetCrmRolePermissionResponseBodyPermissionsFieldScopes()
                self.field_scopes.append(temp_model.from_map(k))
        self.managing_scope_list = []
        if m.get('managingScopeList') is not None:
            for k in m.get('managingScopeList'):
                temp_model = GetCrmRolePermissionResponseBodyPermissionsManagingScopeList()
                self.managing_scope_list.append(temp_model.from_map(k))
        self.operate_scopes = []
        if m.get('operateScopes') is not None:
            for k in m.get('operateScopes'):
                temp_model = GetCrmRolePermissionResponseBodyPermissionsOperateScopes()
                self.operate_scopes.append(temp_model.from_map(k))
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('roleId') is not None:
            self.role_id = m.get('roleId')
        self.role_member_list = []
        if m.get('roleMemberList') is not None:
            for k in m.get('roleMemberList'):
                temp_model = GetCrmRolePermissionResponseBodyPermissionsRoleMemberList()
                self.role_member_list.append(temp_model.from_map(k))
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        return self


class GetCrmRolePermissionResponseBody(TeaModel):
    def __init__(
        self,
        permissions: List[GetCrmRolePermissionResponseBodyPermissions] = None,
    ):
        self.permissions = permissions

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['permissions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.permissions = []
        if m.get('permissions') is not None:
            for k in m.get('permissions'):
                temp_model = GetCrmRolePermissionResponseBodyPermissions()
                self.permissions.append(temp_model.from_map(k))
        return self


class GetCrmRolePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCrmRolePermissionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCrmRolePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomerTracksByRelationIdHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetCustomerTracksByRelationIdRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        relation_id: str = None,
        type_group: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.relation_id = relation_id
        self.type_group = type_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.relation_id is not None:
            result['relationId'] = self.relation_id
        if self.type_group is not None:
            result['typeGroup'] = self.type_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('relationId') is not None:
            self.relation_id = m.get('relationId')
        if m.get('typeGroup') is not None:
            self.type_group = m.get('typeGroup')
        return self


class GetCustomerTracksByRelationIdResponseBodyResultListIsvInfo(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        org_name: str = None,
    ):
        self.app_name = app_name
        self.org_name = org_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.org_name is not None:
            result['orgName'] = self.org_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')
        return self


class GetCustomerTracksByRelationIdResponseBodyResultList(TeaModel):
    def __init__(
        self,
        content: str = None,
        creator_name: str = None,
        detail: Dict[str, str] = None,
        format: str = None,
        gmt_create: str = None,
        isv_info: GetCustomerTracksByRelationIdResponseBodyResultListIsvInfo = None,
        title: str = None,
        type: int = None,
        type_group: int = None,
    ):
        self.content = content
        self.creator_name = creator_name
        self.detail = detail
        self.format = format
        self.gmt_create = gmt_create
        self.isv_info = isv_info
        self.title = title
        self.type = type
        self.type_group = type_group

    def validate(self):
        if self.isv_info:
            self.isv_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.detail is not None:
            result['detail'] = self.detail
        if self.format is not None:
            result['format'] = self.format
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.isv_info is not None:
            result['isvInfo'] = self.isv_info.to_map()
        if self.title is not None:
            result['title'] = self.title
        if self.type is not None:
            result['type'] = self.type
        if self.type_group is not None:
            result['typeGroup'] = self.type_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('isvInfo') is not None:
            temp_model = GetCustomerTracksByRelationIdResponseBodyResultListIsvInfo()
            self.isv_info = temp_model.from_map(m['isvInfo'])
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('typeGroup') is not None:
            self.type_group = m.get('typeGroup')
        return self


class GetCustomerTracksByRelationIdResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        next_token: str = None,
        result_list: List[GetCustomerTracksByRelationIdResponseBodyResultList] = None,
    ):
        self.has_more = has_more
        self.next_token = next_token
        self.result_list = result_list

    def validate(self):
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['resultList'] = []
        if self.result_list is not None:
            for k in self.result_list:
                result['resultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.result_list = []
        if m.get('resultList') is not None:
            for k in m.get('resultList'):
                temp_model = GetCustomerTracksByRelationIdResponseBodyResultList()
                self.result_list.append(temp_model.from_map(k))
        return self


class GetCustomerTracksByRelationIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCustomerTracksByRelationIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCustomerTracksByRelationIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupSetHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetGroupSetRequest(TeaModel):
    def __init__(
        self,
        open_group_set_id: str = None,
    ):
        self.open_group_set_id = open_group_set_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        return self


class GetGroupSetResponseBodyManager(TeaModel):
    def __init__(
        self,
        name: str = None,
        user_id: str = None,
    ):
        self.name = name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetGroupSetResponseBodyOwner(TeaModel):
    def __init__(
        self,
        name: str = None,
        user_id: str = None,
    ):
        self.name = name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetGroupSetResponseBody(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        group_chat_count: int = None,
        invite_link: str = None,
        last_open_conversation_id: str = None,
        manager: List[GetGroupSetResponseBodyManager] = None,
        manager_user_ids: str = None,
        member_count: int = None,
        member_quota: int = None,
        name: str = None,
        notice: str = None,
        notice_toped: int = None,
        open_group_set_id: str = None,
        owner: GetGroupSetResponseBodyOwner = None,
        owner_user_id: str = None,
        relation_type: str = None,
        template_id: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.group_chat_count = group_chat_count
        self.invite_link = invite_link
        self.last_open_conversation_id = last_open_conversation_id
        self.manager = manager
        self.manager_user_ids = manager_user_ids
        self.member_count = member_count
        self.member_quota = member_quota
        self.name = name
        self.notice = notice
        self.notice_toped = notice_toped
        self.open_group_set_id = open_group_set_id
        self.owner = owner
        self.owner_user_id = owner_user_id
        self.relation_type = relation_type
        self.template_id = template_id

    def validate(self):
        if self.manager:
            for k in self.manager:
                if k:
                    k.validate()
        if self.owner:
            self.owner.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.group_chat_count is not None:
            result['groupChatCount'] = self.group_chat_count
        if self.invite_link is not None:
            result['inviteLink'] = self.invite_link
        if self.last_open_conversation_id is not None:
            result['lastOpenConversationId'] = self.last_open_conversation_id
        result['manager'] = []
        if self.manager is not None:
            for k in self.manager:
                result['manager'].append(k.to_map() if k else None)
        if self.manager_user_ids is not None:
            result['managerUserIds'] = self.manager_user_ids
        if self.member_count is not None:
            result['memberCount'] = self.member_count
        if self.member_quota is not None:
            result['memberQuota'] = self.member_quota
        if self.name is not None:
            result['name'] = self.name
        if self.notice is not None:
            result['notice'] = self.notice
        if self.notice_toped is not None:
            result['noticeToped'] = self.notice_toped
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.owner is not None:
            result['owner'] = self.owner.to_map()
        if self.owner_user_id is not None:
            result['ownerUserId'] = self.owner_user_id
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('groupChatCount') is not None:
            self.group_chat_count = m.get('groupChatCount')
        if m.get('inviteLink') is not None:
            self.invite_link = m.get('inviteLink')
        if m.get('lastOpenConversationId') is not None:
            self.last_open_conversation_id = m.get('lastOpenConversationId')
        self.manager = []
        if m.get('manager') is not None:
            for k in m.get('manager'):
                temp_model = GetGroupSetResponseBodyManager()
                self.manager.append(temp_model.from_map(k))
        if m.get('managerUserIds') is not None:
            self.manager_user_ids = m.get('managerUserIds')
        if m.get('memberCount') is not None:
            self.member_count = m.get('memberCount')
        if m.get('memberQuota') is not None:
            self.member_quota = m.get('memberQuota')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('notice') is not None:
            self.notice = m.get('notice')
        if m.get('noticeToped') is not None:
            self.notice_toped = m.get('noticeToped')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('owner') is not None:
            temp_model = GetGroupSetResponseBodyOwner()
            self.owner = temp_model.from_map(m['owner'])
        if m.get('ownerUserId') is not None:
            self.owner_user_id = m.get('ownerUserId')
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class GetGroupSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGroupSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGroupSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOfficialAccountContactInfoHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetOfficialAccountContactInfoResponseBody(TeaModel):
    def __init__(
        self,
        auth_items: List[str] = None,
        corp_name: str = None,
        mobile: str = None,
        state_code: str = None,
        union_id: str = None,
        user_infos: List[str] = None,
    ):
        self.auth_items = auth_items
        self.corp_name = corp_name
        self.mobile = mobile
        self.state_code = state_code
        self.union_id = union_id
        self.user_infos = user_infos

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_items is not None:
            result['authItems'] = self.auth_items
        if self.corp_name is not None:
            result['corpName'] = self.corp_name
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.state_code is not None:
            result['stateCode'] = self.state_code
        if self.union_id is not None:
            result['unionId'] = self.union_id
        if self.user_infos is not None:
            result['userInfos'] = self.user_infos
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authItems') is not None:
            self.auth_items = m.get('authItems')
        if m.get('corpName') is not None:
            self.corp_name = m.get('corpName')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('stateCode') is not None:
            self.state_code = m.get('stateCode')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        if m.get('userInfos') is not None:
            self.user_infos = m.get('userInfos')
        return self


class GetOfficialAccountContactInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOfficialAccountContactInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetOfficialAccountContactInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOfficialAccountContactsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetOfficialAccountContactsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class GetOfficialAccountContactsResponseBodyValuesContactsPermission(TeaModel):
    def __init__(
        self,
        owner_staff_ids: List[str] = None,
        participant_staff_ids: List[str] = None,
    ):
        self.owner_staff_ids = owner_staff_ids
        self.participant_staff_ids = participant_staff_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_staff_ids is not None:
            result['ownerStaffIds'] = self.owner_staff_ids
        if self.participant_staff_ids is not None:
            result['participantStaffIds'] = self.participant_staff_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ownerStaffIds') is not None:
            self.owner_staff_ids = m.get('ownerStaffIds')
        if m.get('participantStaffIds') is not None:
            self.participant_staff_ids = m.get('participantStaffIds')
        return self


class GetOfficialAccountContactsResponseBodyValuesContacts(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        creator_nick: str = None,
        creator_user_id: str = None,
        data: Dict[str, Any] = None,
        extend_data: Dict[str, Any] = None,
        instance_id: str = None,
        modify_time: str = None,
        permission: GetOfficialAccountContactsResponseBodyValuesContactsPermission = None,
    ):
        self.create_time = create_time
        self.creator_nick = creator_nick
        self.creator_user_id = creator_user_id
        self.data = data
        self.extend_data = extend_data
        self.instance_id = instance_id
        self.modify_time = modify_time
        self.permission = permission

    def validate(self):
        if self.permission:
            self.permission.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_nick is not None:
            result['creatorNick'] = self.creator_nick
        if self.creator_user_id is not None:
            result['creatorUserId'] = self.creator_user_id
        if self.data is not None:
            result['data'] = self.data
        if self.extend_data is not None:
            result['extendData'] = self.extend_data
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.permission is not None:
            result['permission'] = self.permission.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorNick') is not None:
            self.creator_nick = m.get('creatorNick')
        if m.get('creatorUserId') is not None:
            self.creator_user_id = m.get('creatorUserId')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('extendData') is not None:
            self.extend_data = m.get('extendData')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('permission') is not None:
            temp_model = GetOfficialAccountContactsResponseBodyValuesContactsPermission()
            self.permission = temp_model.from_map(m['permission'])
        return self


class GetOfficialAccountContactsResponseBodyValues(TeaModel):
    def __init__(
        self,
        contacts: List[GetOfficialAccountContactsResponseBodyValuesContacts] = None,
        user_id: str = None,
    ):
        self.contacts = contacts
        self.user_id = user_id

    def validate(self):
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['contacts'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contacts = []
        if m.get('contacts') is not None:
            for k in m.get('contacts'):
                temp_model = GetOfficialAccountContactsResponseBodyValuesContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetOfficialAccountContactsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        values: List[GetOfficialAccountContactsResponseBodyValues] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['values'] = []
        if self.values is not None:
            for k in self.values:
                result['values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.values = []
        if m.get('values') is not None:
            for k in m.get('values'):
                temp_model = GetOfficialAccountContactsResponseBodyValues()
                self.values.append(temp_model.from_map(k))
        return self


class GetOfficialAccountContactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOfficialAccountContactsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetOfficialAccountContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOfficialAccountOTOMessageResultHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetOfficialAccountOTOMessageResultRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        open_push_id: str = None,
    ):
        self.account_id = account_id
        self.open_push_id = open_push_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.open_push_id is not None:
            result['openPushId'] = self.open_push_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('openPushId') is not None:
            self.open_push_id = m.get('openPushId')
        return self


class GetOfficialAccountOTOMessageResultResponseBodyResult(TeaModel):
    def __init__(
        self,
        read_user_id_list: List[str] = None,
        status: int = None,
    ):
        self.read_user_id_list = read_user_id_list
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.read_user_id_list is not None:
            result['readUserIdList'] = self.read_user_id_list
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('readUserIdList') is not None:
            self.read_user_id_list = m.get('readUserIdList')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetOfficialAccountOTOMessageResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetOfficialAccountOTOMessageResultResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetOfficialAccountOTOMessageResultResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetOfficialAccountOTOMessageResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOfficialAccountOTOMessageResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetOfficialAccountOTOMessageResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRelationUkSettingHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetRelationUkSettingRequest(TeaModel):
    def __init__(
        self,
        relation_type: str = None,
    ):
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        return self


class GetRelationUkSettingResponseBodyResult(TeaModel):
    def __init__(
        self,
        biz_alias: str = None,
        field_id: str = None,
    ):
        self.biz_alias = biz_alias
        self.field_id = field_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_alias is not None:
            result['bizAlias'] = self.biz_alias
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizAlias') is not None:
            self.biz_alias = m.get('bizAlias')
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        return self


class GetRelationUkSettingResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetRelationUkSettingResponseBodyResult] = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = GetRelationUkSettingResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetRelationUkSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRelationUkSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRelationUkSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinGroupSetHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class JoinGroupSetRequestBizDataList(TeaModel):
    def __init__(
        self,
        extend_value: str = None,
        key: str = None,
        value: str = None,
    ):
        self.extend_value = extend_value
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_value is not None:
            result['extendValue'] = self.extend_value
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extendValue') is not None:
            self.extend_value = m.get('extendValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class JoinGroupSetRequest(TeaModel):
    def __init__(
        self,
        biz_data_list: List[JoinGroupSetRequestBizDataList] = None,
        corp_id: str = None,
        open_group_set_id: str = None,
        union_id: str = None,
    ):
        self.biz_data_list = biz_data_list
        self.corp_id = corp_id
        self.open_group_set_id = open_group_set_id
        self.union_id = union_id

    def validate(self):
        if self.biz_data_list:
            for k in self.biz_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['bizDataList'] = []
        if self.biz_data_list is not None:
            for k in self.biz_data_list:
                result['bizDataList'].append(k.to_map() if k else None)
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_data_list = []
        if m.get('bizDataList') is not None:
            for k in m.get('bizDataList'):
                temp_model = JoinGroupSetRequestBizDataList()
                self.biz_data_list.append(temp_model.from_map(k))
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class JoinGroupSetResponseBody(TeaModel):
    def __init__(
        self,
        chat_id: str = None,
        open_conversation_id: str = None,
    ):
        self.chat_id = chat_id
        self.open_conversation_id = open_conversation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        return self


class JoinGroupSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: JoinGroupSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = JoinGroupSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCrmPersonalCustomersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class ListCrmPersonalCustomersRequest(TeaModel):
    def __init__(
        self,
        body: List[str] = None,
        current_operator_user_id: str = None,
        relation_type: str = None,
    ):
        self.body = body
        self.current_operator_user_id = current_operator_user_id
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.current_operator_user_id is not None:
            result['currentOperatorUserId'] = self.current_operator_user_id
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('currentOperatorUserId') is not None:
            self.current_operator_user_id = m.get('currentOperatorUserId')
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        return self


class ListCrmPersonalCustomersResponseBodyResultPermission(TeaModel):
    def __init__(
        self,
        owner_staff_ids: List[str] = None,
        participant_staff_ids: List[str] = None,
    ):
        self.owner_staff_ids = owner_staff_ids
        self.participant_staff_ids = participant_staff_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_staff_ids is not None:
            result['ownerStaffIds'] = self.owner_staff_ids
        if self.participant_staff_ids is not None:
            result['participantStaffIds'] = self.participant_staff_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ownerStaffIds') is not None:
            self.owner_staff_ids = m.get('ownerStaffIds')
        if m.get('participantStaffIds') is not None:
            self.participant_staff_ids = m.get('participantStaffIds')
        return self


class ListCrmPersonalCustomersResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_uuid: str = None,
        creator_nick: str = None,
        creator_user_id: str = None,
        data: Dict[str, Any] = None,
        extend_data: Dict[str, Any] = None,
        form_code: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        instance_id: str = None,
        object_type: str = None,
        permission: ListCrmPersonalCustomersResponseBodyResultPermission = None,
        proc_inst_status: str = None,
        proc_out_result: str = None,
    ):
        self.app_uuid = app_uuid
        self.creator_nick = creator_nick
        self.creator_user_id = creator_user_id
        self.data = data
        self.extend_data = extend_data
        self.form_code = form_code
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.instance_id = instance_id
        self.object_type = object_type
        self.permission = permission
        self.proc_inst_status = proc_inst_status
        self.proc_out_result = proc_out_result

    def validate(self):
        if self.permission:
            self.permission.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uuid is not None:
            result['appUuid'] = self.app_uuid
        if self.creator_nick is not None:
            result['creatorNick'] = self.creator_nick
        if self.creator_user_id is not None:
            result['creatorUserId'] = self.creator_user_id
        if self.data is not None:
            result['data'] = self.data
        if self.extend_data is not None:
            result['extendData'] = self.extend_data
        if self.form_code is not None:
            result['formCode'] = self.form_code
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.object_type is not None:
            result['objectType'] = self.object_type
        if self.permission is not None:
            result['permission'] = self.permission.to_map()
        if self.proc_inst_status is not None:
            result['procInstStatus'] = self.proc_inst_status
        if self.proc_out_result is not None:
            result['procOutResult'] = self.proc_out_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appUuid') is not None:
            self.app_uuid = m.get('appUuid')
        if m.get('creatorNick') is not None:
            self.creator_nick = m.get('creatorNick')
        if m.get('creatorUserId') is not None:
            self.creator_user_id = m.get('creatorUserId')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('extendData') is not None:
            self.extend_data = m.get('extendData')
        if m.get('formCode') is not None:
            self.form_code = m.get('formCode')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        if m.get('permission') is not None:
            temp_model = ListCrmPersonalCustomersResponseBodyResultPermission()
            self.permission = temp_model.from_map(m['permission'])
        if m.get('procInstStatus') is not None:
            self.proc_inst_status = m.get('procInstStatus')
        if m.get('procOutResult') is not None:
            self.proc_out_result = m.get('procOutResult')
        return self


class ListCrmPersonalCustomersResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListCrmPersonalCustomersResponseBodyResult] = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListCrmPersonalCustomersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListCrmPersonalCustomersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCrmPersonalCustomersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCrmPersonalCustomersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupSetHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class ListGroupSetRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        query_dsl: str = None,
        relation_type: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.query_dsl = query_dsl
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.query_dsl is not None:
            result['queryDsl'] = self.query_dsl
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('queryDsl') is not None:
            self.query_dsl = m.get('queryDsl')
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        return self


class ListGroupSetResponseBodyResultListManager(TeaModel):
    def __init__(
        self,
        name: str = None,
        user_id: str = None,
    ):
        self.name = name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListGroupSetResponseBodyResultListOwner(TeaModel):
    def __init__(
        self,
        name: str = None,
        user_id: str = None,
    ):
        self.name = name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListGroupSetResponseBodyResultList(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        group_chat_count: int = None,
        last_open_conversation_id: str = None,
        manager: List[ListGroupSetResponseBodyResultListManager] = None,
        manager_user_ids: str = None,
        member_count: int = None,
        member_quota: int = None,
        name: str = None,
        notice: str = None,
        notice_toped: int = None,
        open_group_set_id: str = None,
        owner: ListGroupSetResponseBodyResultListOwner = None,
        owner_user_id: str = None,
        relation_type: str = None,
        template_id: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.group_chat_count = group_chat_count
        self.last_open_conversation_id = last_open_conversation_id
        self.manager = manager
        self.manager_user_ids = manager_user_ids
        self.member_count = member_count
        self.member_quota = member_quota
        self.name = name
        self.notice = notice
        self.notice_toped = notice_toped
        self.open_group_set_id = open_group_set_id
        self.owner = owner
        self.owner_user_id = owner_user_id
        self.relation_type = relation_type
        self.template_id = template_id

    def validate(self):
        if self.manager:
            for k in self.manager:
                if k:
                    k.validate()
        if self.owner:
            self.owner.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.group_chat_count is not None:
            result['groupChatCount'] = self.group_chat_count
        if self.last_open_conversation_id is not None:
            result['lastOpenConversationId'] = self.last_open_conversation_id
        result['manager'] = []
        if self.manager is not None:
            for k in self.manager:
                result['manager'].append(k.to_map() if k else None)
        if self.manager_user_ids is not None:
            result['managerUserIds'] = self.manager_user_ids
        if self.member_count is not None:
            result['memberCount'] = self.member_count
        if self.member_quota is not None:
            result['memberQuota'] = self.member_quota
        if self.name is not None:
            result['name'] = self.name
        if self.notice is not None:
            result['notice'] = self.notice
        if self.notice_toped is not None:
            result['noticeToped'] = self.notice_toped
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.owner is not None:
            result['owner'] = self.owner.to_map()
        if self.owner_user_id is not None:
            result['ownerUserId'] = self.owner_user_id
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('groupChatCount') is not None:
            self.group_chat_count = m.get('groupChatCount')
        if m.get('lastOpenConversationId') is not None:
            self.last_open_conversation_id = m.get('lastOpenConversationId')
        self.manager = []
        if m.get('manager') is not None:
            for k in m.get('manager'):
                temp_model = ListGroupSetResponseBodyResultListManager()
                self.manager.append(temp_model.from_map(k))
        if m.get('managerUserIds') is not None:
            self.manager_user_ids = m.get('managerUserIds')
        if m.get('memberCount') is not None:
            self.member_count = m.get('memberCount')
        if m.get('memberQuota') is not None:
            self.member_quota = m.get('memberQuota')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('notice') is not None:
            self.notice = m.get('notice')
        if m.get('noticeToped') is not None:
            self.notice_toped = m.get('noticeToped')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('owner') is not None:
            temp_model = ListGroupSetResponseBodyResultListOwner()
            self.owner = temp_model.from_map(m['owner'])
        if m.get('ownerUserId') is not None:
            self.owner_user_id = m.get('ownerUserId')
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class ListGroupSetResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        next_token: str = None,
        result_list: List[ListGroupSetResponseBodyResultList] = None,
        total_count: int = None,
    ):
        self.has_more = has_more
        self.next_token = next_token
        self.result_list = result_list
        self.total_count = total_count

    def validate(self):
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['resultList'] = []
        if self.result_list is not None:
            for k in self.result_list:
                result['resultList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.result_list = []
        if m.get('resultList') is not None:
            for k in m.get('resultList'):
                temp_model = ListGroupSetResponseBodyResultList()
                self.result_list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListGroupSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGroupSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListGroupSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAllCustomerHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class QueryAllCustomerRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        object_type: str = None,
        operator_user_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.object_type = object_type
        self.operator_user_id = operator_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.object_type is not None:
            result['objectType'] = self.object_type
        if self.operator_user_id is not None:
            result['operatorUserId'] = self.operator_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        if m.get('operatorUserId') is not None:
            self.operator_user_id = m.get('operatorUserId')
        return self


class QueryAllCustomerResponseBodyResultValuesPermission(TeaModel):
    def __init__(
        self,
        owner_staff_ids: List[str] = None,
        participant_staff_ids: List[str] = None,
    ):
        self.owner_staff_ids = owner_staff_ids
        self.participant_staff_ids = participant_staff_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_staff_ids is not None:
            result['ownerStaffIds'] = self.owner_staff_ids
        if self.participant_staff_ids is not None:
            result['participantStaffIds'] = self.participant_staff_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ownerStaffIds') is not None:
            self.owner_staff_ids = m.get('ownerStaffIds')
        if m.get('participantStaffIds') is not None:
            self.participant_staff_ids = m.get('participantStaffIds')
        return self


class QueryAllCustomerResponseBodyResultValues(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        creator_nick: str = None,
        creator_user_id: str = None,
        data: Dict[str, Any] = None,
        extend_data: Dict[str, Any] = None,
        instance_id: str = None,
        modify_time: str = None,
        object_type: str = None,
        permission: QueryAllCustomerResponseBodyResultValuesPermission = None,
        process_instance_status: str = None,
        process_out_result: str = None,
    ):
        self.create_time = create_time
        self.creator_nick = creator_nick
        self.creator_user_id = creator_user_id
        self.data = data
        self.extend_data = extend_data
        self.instance_id = instance_id
        self.modify_time = modify_time
        self.object_type = object_type
        self.permission = permission
        self.process_instance_status = process_instance_status
        self.process_out_result = process_out_result

    def validate(self):
        if self.permission:
            self.permission.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_nick is not None:
            result['creatorNick'] = self.creator_nick
        if self.creator_user_id is not None:
            result['creatorUserId'] = self.creator_user_id
        if self.data is not None:
            result['data'] = self.data
        if self.extend_data is not None:
            result['extendData'] = self.extend_data
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.object_type is not None:
            result['objectType'] = self.object_type
        if self.permission is not None:
            result['permission'] = self.permission.to_map()
        if self.process_instance_status is not None:
            result['processInstanceStatus'] = self.process_instance_status
        if self.process_out_result is not None:
            result['processOutResult'] = self.process_out_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorNick') is not None:
            self.creator_nick = m.get('creatorNick')
        if m.get('creatorUserId') is not None:
            self.creator_user_id = m.get('creatorUserId')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('extendData') is not None:
            self.extend_data = m.get('extendData')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        if m.get('permission') is not None:
            temp_model = QueryAllCustomerResponseBodyResultValuesPermission()
            self.permission = temp_model.from_map(m['permission'])
        if m.get('processInstanceStatus') is not None:
            self.process_instance_status = m.get('processInstanceStatus')
        if m.get('processOutResult') is not None:
            self.process_out_result = m.get('processOutResult')
        return self


class QueryAllCustomerResponseBodyResult(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        values: List[QueryAllCustomerResponseBodyResultValues] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['values'] = []
        if self.values is not None:
            for k in self.values:
                result['values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.values = []
        if m.get('values') is not None:
            for k in m.get('values'):
                temp_model = QueryAllCustomerResponseBodyResultValues()
                self.values.append(temp_model.from_map(k))
        return self


class QueryAllCustomerResponseBody(TeaModel):
    def __init__(
        self,
        result: QueryAllCustomerResponseBodyResult = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = QueryAllCustomerResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class QueryAllCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAllCustomerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryAllCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAllTracksHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class QueryAllTracksRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.order is not None:
            result['order'] = self.order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('order') is not None:
            self.order = m.get('order')
        return self


class QueryAllTracksResponseBodyValues(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        creator: str = None,
        customer_id: str = None,
        gmt_create: int = None,
        id: str = None,
        sub_type: int = None,
        type: int = None,
    ):
        self.biz_id = biz_id
        self.creator = creator
        self.customer_id = customer_id
        self.gmt_create = gmt_create
        self.id = id
        self.sub_type = sub_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.creator is not None:
            result['creator'] = self.creator
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.id is not None:
            result['id'] = self.id
        if self.sub_type is not None:
            result['subType'] = self.sub_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('subType') is not None:
            self.sub_type = m.get('subType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class QueryAllTracksResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        max_results: int = None,
        next_token: str = None,
        values: List[QueryAllTracksResponseBodyValues] = None,
    ):
        self.has_more = has_more
        self.max_results = max_results
        self.next_token = next_token
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['values'] = []
        if self.values is not None:
            for k in self.values:
                result['values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.values = []
        if m.get('values') is not None:
            for k in m.get('values'):
                temp_model = QueryAllTracksResponseBodyValues()
                self.values.append(temp_model.from_map(k))
        return self


class QueryAllTracksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAllTracksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryAllTracksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCrmGroupChatsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class QueryCrmGroupChatsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        query_dsl: str = None,
        relation_type: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.query_dsl = query_dsl
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.query_dsl is not None:
            result['queryDsl'] = self.query_dsl
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('queryDsl') is not None:
            self.query_dsl = m.get('queryDsl')
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        return self


class QueryCrmGroupChatsResponseBodyResultList(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        member_count: int = None,
        name: str = None,
        open_conversation_id: str = None,
        open_group_set_id: str = None,
        owner_user_id: str = None,
        owner_user_name: str = None,
    ):
        self.gmt_create = gmt_create
        self.member_count = member_count
        self.name = name
        self.open_conversation_id = open_conversation_id
        self.open_group_set_id = open_group_set_id
        self.owner_user_id = owner_user_id
        self.owner_user_name = owner_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.member_count is not None:
            result['memberCount'] = self.member_count
        if self.name is not None:
            result['name'] = self.name
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.owner_user_id is not None:
            result['ownerUserId'] = self.owner_user_id
        if self.owner_user_name is not None:
            result['ownerUserName'] = self.owner_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('memberCount') is not None:
            self.member_count = m.get('memberCount')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('ownerUserId') is not None:
            self.owner_user_id = m.get('ownerUserId')
        if m.get('ownerUserName') is not None:
            self.owner_user_name = m.get('ownerUserName')
        return self


class QueryCrmGroupChatsResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        next_token: str = None,
        result_list: List[QueryCrmGroupChatsResponseBodyResultList] = None,
        total_count: int = None,
    ):
        self.has_more = has_more
        self.next_token = next_token
        self.result_list = result_list
        self.total_count = total_count

    def validate(self):
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['resultList'] = []
        if self.result_list is not None:
            for k in self.result_list:
                result['resultList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.result_list = []
        if m.get('resultList') is not None:
            for k in m.get('resultList'):
                temp_model = QueryCrmGroupChatsResponseBodyResultList()
                self.result_list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class QueryCrmGroupChatsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCrmGroupChatsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryCrmGroupChatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCrmPersonalCustomerHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class QueryCrmPersonalCustomerRequest(TeaModel):
    def __init__(
        self,
        current_operator_user_id: str = None,
        max_results: int = None,
        next_token: str = None,
        query_dsl: str = None,
        relation_type: str = None,
    ):
        self.current_operator_user_id = current_operator_user_id
        self.max_results = max_results
        self.next_token = next_token
        self.query_dsl = query_dsl
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_operator_user_id is not None:
            result['currentOperatorUserId'] = self.current_operator_user_id
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.query_dsl is not None:
            result['queryDsl'] = self.query_dsl
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentOperatorUserId') is not None:
            self.current_operator_user_id = m.get('currentOperatorUserId')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('queryDsl') is not None:
            self.query_dsl = m.get('queryDsl')
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        return self


class QueryCrmPersonalCustomerResponseBodyValuesPermission(TeaModel):
    def __init__(
        self,
        owner_staff_ids: List[str] = None,
        participant_staff_ids: List[str] = None,
    ):
        self.owner_staff_ids = owner_staff_ids
        self.participant_staff_ids = participant_staff_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_staff_ids is not None:
            result['ownerStaffIds'] = self.owner_staff_ids
        if self.participant_staff_ids is not None:
            result['participantStaffIds'] = self.participant_staff_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ownerStaffIds') is not None:
            self.owner_staff_ids = m.get('ownerStaffIds')
        if m.get('participantStaffIds') is not None:
            self.participant_staff_ids = m.get('participantStaffIds')
        return self


class QueryCrmPersonalCustomerResponseBodyValues(TeaModel):
    def __init__(
        self,
        creator_nick: str = None,
        creator_user_id: str = None,
        data: Dict[str, Any] = None,
        extend_data: Dict[str, Any] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        instance_id: str = None,
        object_type: str = None,
        permission: QueryCrmPersonalCustomerResponseBodyValuesPermission = None,
        proc_inst_status: str = None,
        proc_out_result: str = None,
    ):
        self.creator_nick = creator_nick
        self.creator_user_id = creator_user_id
        self.data = data
        self.extend_data = extend_data
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.instance_id = instance_id
        self.object_type = object_type
        self.permission = permission
        self.proc_inst_status = proc_inst_status
        self.proc_out_result = proc_out_result

    def validate(self):
        if self.permission:
            self.permission.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_nick is not None:
            result['creatorNick'] = self.creator_nick
        if self.creator_user_id is not None:
            result['creatorUserId'] = self.creator_user_id
        if self.data is not None:
            result['data'] = self.data
        if self.extend_data is not None:
            result['extendData'] = self.extend_data
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.object_type is not None:
            result['objectType'] = self.object_type
        if self.permission is not None:
            result['permission'] = self.permission.to_map()
        if self.proc_inst_status is not None:
            result['procInstStatus'] = self.proc_inst_status
        if self.proc_out_result is not None:
            result['procOutResult'] = self.proc_out_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorNick') is not None:
            self.creator_nick = m.get('creatorNick')
        if m.get('creatorUserId') is not None:
            self.creator_user_id = m.get('creatorUserId')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('extendData') is not None:
            self.extend_data = m.get('extendData')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        if m.get('permission') is not None:
            temp_model = QueryCrmPersonalCustomerResponseBodyValuesPermission()
            self.permission = temp_model.from_map(m['permission'])
        if m.get('procInstStatus') is not None:
            self.proc_inst_status = m.get('procInstStatus')
        if m.get('procOutResult') is not None:
            self.proc_out_result = m.get('procOutResult')
        return self


class QueryCrmPersonalCustomerResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
        values: List[QueryCrmPersonalCustomerResponseBodyValues] = None,
    ):
        self.has_more = has_more
        self.max_results = max_results
        self.next_token = next_token
        self.total_count = total_count
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        result['values'] = []
        if self.values is not None:
            for k in self.values:
                result['values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        self.values = []
        if m.get('values') is not None:
            for k in m.get('values'):
                temp_model = QueryCrmPersonalCustomerResponseBodyValues()
                self.values.append(temp_model.from_map(k))
        return self


class QueryCrmPersonalCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCrmPersonalCustomerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryCrmPersonalCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGlobalInfoHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class QueryGlobalInfoRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryGlobalInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        oem_enable: bool = None,
    ):
        self.oem_enable = oem_enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oem_enable is not None:
            result['oemEnable'] = self.oem_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('oemEnable') is not None:
            self.oem_enable = m.get('oemEnable')
        return self


class QueryGlobalInfoResponseBody(TeaModel):
    def __init__(
        self,
        result: QueryGlobalInfoResponseBodyResult = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = QueryGlobalInfoResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class QueryGlobalInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryGlobalInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryGlobalInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOfficialAccountUserBasicInfoHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class QueryOfficialAccountUserBasicInfoRequest(TeaModel):
    def __init__(
        self,
        binding_token: str = None,
        union_id: str = None,
    ):
        self.binding_token = binding_token
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binding_token is not None:
            result['bindingToken'] = self.binding_token
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bindingToken') is not None:
            self.binding_token = m.get('bindingToken')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class QueryOfficialAccountUserBasicInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class QueryOfficialAccountUserBasicInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryOfficialAccountUserBasicInfoResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = QueryOfficialAccountUserBasicInfoResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class QueryOfficialAccountUserBasicInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryOfficialAccountUserBasicInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryOfficialAccountUserBasicInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRelationDatasByTargetIdHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class QueryRelationDatasByTargetIdRequest(TeaModel):
    def __init__(
        self,
        relation_type: str = None,
    ):
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        return self


class QueryRelationDatasByTargetIdResponseBodyRelationsBizDataList(TeaModel):
    def __init__(
        self,
        extend_value: str = None,
        key: str = None,
        value: str = None,
    ):
        self.extend_value = extend_value
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_value is not None:
            result['extendValue'] = self.extend_value
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extendValue') is not None:
            self.extend_value = m.get('extendValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class QueryRelationDatasByTargetIdResponseBodyRelations(TeaModel):
    def __init__(
        self,
        biz_data_list: List[QueryRelationDatasByTargetIdResponseBodyRelationsBizDataList] = None,
        open_conversation_ids: List[str] = None,
        relation_id: str = None,
        relation_type: str = None,
    ):
        self.biz_data_list = biz_data_list
        self.open_conversation_ids = open_conversation_ids
        self.relation_id = relation_id
        self.relation_type = relation_type

    def validate(self):
        if self.biz_data_list:
            for k in self.biz_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['bizDataList'] = []
        if self.biz_data_list is not None:
            for k in self.biz_data_list:
                result['bizDataList'].append(k.to_map() if k else None)
        if self.open_conversation_ids is not None:
            result['openConversationIds'] = self.open_conversation_ids
        if self.relation_id is not None:
            result['relationId'] = self.relation_id
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_data_list = []
        if m.get('bizDataList') is not None:
            for k in m.get('bizDataList'):
                temp_model = QueryRelationDatasByTargetIdResponseBodyRelationsBizDataList()
                self.biz_data_list.append(temp_model.from_map(k))
        if m.get('openConversationIds') is not None:
            self.open_conversation_ids = m.get('openConversationIds')
        if m.get('relationId') is not None:
            self.relation_id = m.get('relationId')
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        return self


class QueryRelationDatasByTargetIdResponseBody(TeaModel):
    def __init__(
        self,
        relations: List[QueryRelationDatasByTargetIdResponseBodyRelations] = None,
    ):
        self.relations = relations

    def validate(self):
        if self.relations:
            for k in self.relations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['relations'] = []
        if self.relations is not None:
            for k in self.relations:
                result['relations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.relations = []
        if m.get('relations') is not None:
            for k in m.get('relations'):
                temp_model = QueryRelationDatasByTargetIdResponseBodyRelations()
                self.relations.append(temp_model.from_map(k))
        return self


class QueryRelationDatasByTargetIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRelationDatasByTargetIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryRelationDatasByTargetIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecallOfficialAccountOTOMessageHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class RecallOfficialAccountOTOMessageRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        open_push_id: str = None,
    ):
        self.account_id = account_id
        self.open_push_id = open_push_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.open_push_id is not None:
            result['openPushId'] = self.open_push_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('openPushId') is not None:
            self.open_push_id = m.get('openPushId')
        return self


class RecallOfficialAccountOTOMessageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RecallOfficialAccountOTOMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecallOfficialAccountOTOMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecallOfficialAccountOTOMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendOfficialAccountOTOMessageHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList(TeaModel):
    def __init__(
        self,
        action_url: str = None,
        title: str = None,
    ):
        self.action_url = action_url
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_url is not None:
            result['actionUrl'] = self.action_url
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionUrl') is not None:
            self.action_url = m.get('actionUrl')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard(TeaModel):
    def __init__(
        self,
        button_list: List[SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList] = None,
        button_orientation: str = None,
        markdown: str = None,
        single_title: str = None,
        single_url: str = None,
        title: str = None,
    ):
        self.button_list = button_list
        self.button_orientation = button_orientation
        self.markdown = markdown
        self.single_title = single_title
        self.single_url = single_url
        self.title = title

    def validate(self):
        if self.button_list:
            for k in self.button_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['buttonList'] = []
        if self.button_list is not None:
            for k in self.button_list:
                result['buttonList'].append(k.to_map() if k else None)
        if self.button_orientation is not None:
            result['buttonOrientation'] = self.button_orientation
        if self.markdown is not None:
            result['markdown'] = self.markdown
        if self.single_title is not None:
            result['singleTitle'] = self.single_title
        if self.single_url is not None:
            result['singleUrl'] = self.single_url
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.button_list = []
        if m.get('buttonList') is not None:
            for k in m.get('buttonList'):
                temp_model = SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList()
                self.button_list.append(temp_model.from_map(k))
        if m.get('buttonOrientation') is not None:
            self.button_orientation = m.get('buttonOrientation')
        if m.get('markdown') is not None:
            self.markdown = m.get('markdown')
        if m.get('singleTitle') is not None:
            self.single_title = m.get('singleTitle')
        if m.get('singleUrl') is not None:
            self.single_url = m.get('singleUrl')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class SendOfficialAccountOTOMessageRequestDetailMessageBodyImage(TeaModel):
    def __init__(
        self,
        media_id: str = None,
    ):
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['mediaId'] = self.media_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mediaId') is not None:
            self.media_id = m.get('mediaId')
        return self


class SendOfficialAccountOTOMessageRequestDetailMessageBodyLink(TeaModel):
    def __init__(
        self,
        message_url: str = None,
        pic_url: str = None,
        text: str = None,
        title: str = None,
    ):
        self.message_url = message_url
        self.pic_url = pic_url
        self.text = text
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_url is not None:
            result['messageUrl'] = self.message_url
        if self.pic_url is not None:
            result['picUrl'] = self.pic_url
        if self.text is not None:
            result['text'] = self.text
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('messageUrl') is not None:
            self.message_url = m.get('messageUrl')
        if m.get('picUrl') is not None:
            self.pic_url = m.get('picUrl')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class SendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown(TeaModel):
    def __init__(
        self,
        text: str = None,
        title: str = None,
    ):
        self.text = text
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['text'] = self.text
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class SendOfficialAccountOTOMessageRequestDetailMessageBodyText(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class SendOfficialAccountOTOMessageRequestDetailMessageBody(TeaModel):
    def __init__(
        self,
        action_card: SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard = None,
        image: SendOfficialAccountOTOMessageRequestDetailMessageBodyImage = None,
        link: SendOfficialAccountOTOMessageRequestDetailMessageBodyLink = None,
        markdown: SendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown = None,
        text: SendOfficialAccountOTOMessageRequestDetailMessageBodyText = None,
    ):
        self.action_card = action_card
        self.image = image
        self.link = link
        self.markdown = markdown
        self.text = text

    def validate(self):
        if self.action_card:
            self.action_card.validate()
        if self.image:
            self.image.validate()
        if self.link:
            self.link.validate()
        if self.markdown:
            self.markdown.validate()
        if self.text:
            self.text.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_card is not None:
            result['actionCard'] = self.action_card.to_map()
        if self.image is not None:
            result['image'] = self.image.to_map()
        if self.link is not None:
            result['link'] = self.link.to_map()
        if self.markdown is not None:
            result['markdown'] = self.markdown.to_map()
        if self.text is not None:
            result['text'] = self.text.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionCard') is not None:
            temp_model = SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard()
            self.action_card = temp_model.from_map(m['actionCard'])
        if m.get('image') is not None:
            temp_model = SendOfficialAccountOTOMessageRequestDetailMessageBodyImage()
            self.image = temp_model.from_map(m['image'])
        if m.get('link') is not None:
            temp_model = SendOfficialAccountOTOMessageRequestDetailMessageBodyLink()
            self.link = temp_model.from_map(m['link'])
        if m.get('markdown') is not None:
            temp_model = SendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown()
            self.markdown = temp_model.from_map(m['markdown'])
        if m.get('text') is not None:
            temp_model = SendOfficialAccountOTOMessageRequestDetailMessageBodyText()
            self.text = temp_model.from_map(m['text'])
        return self


class SendOfficialAccountOTOMessageRequestDetail(TeaModel):
    def __init__(
        self,
        message_body: SendOfficialAccountOTOMessageRequestDetailMessageBody = None,
        msg_type: str = None,
        union_id: str = None,
        user_id: str = None,
        uuid: str = None,
    ):
        self.message_body = message_body
        self.msg_type = msg_type
        self.union_id = union_id
        self.user_id = user_id
        self.uuid = uuid

    def validate(self):
        if self.message_body:
            self.message_body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_body is not None:
            result['messageBody'] = self.message_body.to_map()
        if self.msg_type is not None:
            result['msgType'] = self.msg_type
        if self.union_id is not None:
            result['unionId'] = self.union_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('messageBody') is not None:
            temp_model = SendOfficialAccountOTOMessageRequestDetailMessageBody()
            self.message_body = temp_model.from_map(m['messageBody'])
        if m.get('msgType') is not None:
            self.msg_type = m.get('msgType')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class SendOfficialAccountOTOMessageRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        biz_id: str = None,
        detail: SendOfficialAccountOTOMessageRequestDetail = None,
    ):
        self.account_id = account_id
        self.biz_id = biz_id
        self.detail = detail

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.detail is not None:
            result['detail'] = self.detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('detail') is not None:
            temp_model = SendOfficialAccountOTOMessageRequestDetail()
            self.detail = temp_model.from_map(m['detail'])
        return self


class SendOfficialAccountOTOMessageResponseBodyResult(TeaModel):
    def __init__(
        self,
        open_push_id: str = None,
    ):
        self.open_push_id = open_push_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_push_id is not None:
            result['openPushId'] = self.open_push_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openPushId') is not None:
            self.open_push_id = m.get('openPushId')
        return self


class SendOfficialAccountOTOMessageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: SendOfficialAccountOTOMessageResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = SendOfficialAccountOTOMessageResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class SendOfficialAccountOTOMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendOfficialAccountOTOMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendOfficialAccountOTOMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendOfficialAccountSNSMessageHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCardButtonList(TeaModel):
    def __init__(
        self,
        action_url: str = None,
        title: str = None,
    ):
        self.action_url = action_url
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_url is not None:
            result['actionUrl'] = self.action_url
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionUrl') is not None:
            self.action_url = m.get('actionUrl')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCard(TeaModel):
    def __init__(
        self,
        button_list: List[SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCardButtonList] = None,
        button_orientation: str = None,
        markdown: str = None,
        single_title: str = None,
        single_url: str = None,
        title: str = None,
    ):
        self.button_list = button_list
        self.button_orientation = button_orientation
        self.markdown = markdown
        self.single_title = single_title
        self.single_url = single_url
        self.title = title

    def validate(self):
        if self.button_list:
            for k in self.button_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['buttonList'] = []
        if self.button_list is not None:
            for k in self.button_list:
                result['buttonList'].append(k.to_map() if k else None)
        if self.button_orientation is not None:
            result['buttonOrientation'] = self.button_orientation
        if self.markdown is not None:
            result['markdown'] = self.markdown
        if self.single_title is not None:
            result['singleTitle'] = self.single_title
        if self.single_url is not None:
            result['singleUrl'] = self.single_url
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.button_list = []
        if m.get('buttonList') is not None:
            for k in m.get('buttonList'):
                temp_model = SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCardButtonList()
                self.button_list.append(temp_model.from_map(k))
        if m.get('buttonOrientation') is not None:
            self.button_orientation = m.get('buttonOrientation')
        if m.get('markdown') is not None:
            self.markdown = m.get('markdown')
        if m.get('singleTitle') is not None:
            self.single_title = m.get('singleTitle')
        if m.get('singleUrl') is not None:
            self.single_url = m.get('singleUrl')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class SendOfficialAccountSNSMessageRequestDetailMessageBodyLink(TeaModel):
    def __init__(
        self,
        message_url: str = None,
        pic_url: str = None,
        text: str = None,
        title: str = None,
    ):
        self.message_url = message_url
        self.pic_url = pic_url
        self.text = text
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_url is not None:
            result['messageUrl'] = self.message_url
        if self.pic_url is not None:
            result['picUrl'] = self.pic_url
        if self.text is not None:
            result['text'] = self.text
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('messageUrl') is not None:
            self.message_url = m.get('messageUrl')
        if m.get('picUrl') is not None:
            self.pic_url = m.get('picUrl')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class SendOfficialAccountSNSMessageRequestDetailMessageBodyMarkdown(TeaModel):
    def __init__(
        self,
        text: str = None,
        title: str = None,
    ):
        self.text = text
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['text'] = self.text
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class SendOfficialAccountSNSMessageRequestDetailMessageBodyText(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class SendOfficialAccountSNSMessageRequestDetailMessageBody(TeaModel):
    def __init__(
        self,
        action_card: SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCard = None,
        link: SendOfficialAccountSNSMessageRequestDetailMessageBodyLink = None,
        markdown: SendOfficialAccountSNSMessageRequestDetailMessageBodyMarkdown = None,
        text: SendOfficialAccountSNSMessageRequestDetailMessageBodyText = None,
    ):
        self.action_card = action_card
        self.link = link
        self.markdown = markdown
        self.text = text

    def validate(self):
        if self.action_card:
            self.action_card.validate()
        if self.link:
            self.link.validate()
        if self.markdown:
            self.markdown.validate()
        if self.text:
            self.text.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_card is not None:
            result['actionCard'] = self.action_card.to_map()
        if self.link is not None:
            result['link'] = self.link.to_map()
        if self.markdown is not None:
            result['markdown'] = self.markdown.to_map()
        if self.text is not None:
            result['text'] = self.text.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionCard') is not None:
            temp_model = SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCard()
            self.action_card = temp_model.from_map(m['actionCard'])
        if m.get('link') is not None:
            temp_model = SendOfficialAccountSNSMessageRequestDetailMessageBodyLink()
            self.link = temp_model.from_map(m['link'])
        if m.get('markdown') is not None:
            temp_model = SendOfficialAccountSNSMessageRequestDetailMessageBodyMarkdown()
            self.markdown = temp_model.from_map(m['markdown'])
        if m.get('text') is not None:
            temp_model = SendOfficialAccountSNSMessageRequestDetailMessageBodyText()
            self.text = temp_model.from_map(m['text'])
        return self


class SendOfficialAccountSNSMessageRequestDetail(TeaModel):
    def __init__(
        self,
        message_body: SendOfficialAccountSNSMessageRequestDetailMessageBody = None,
        msg_type: str = None,
        uuid: str = None,
    ):
        self.message_body = message_body
        self.msg_type = msg_type
        self.uuid = uuid

    def validate(self):
        if self.message_body:
            self.message_body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_body is not None:
            result['messageBody'] = self.message_body.to_map()
        if self.msg_type is not None:
            result['msgType'] = self.msg_type
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('messageBody') is not None:
            temp_model = SendOfficialAccountSNSMessageRequestDetailMessageBody()
            self.message_body = temp_model.from_map(m['messageBody'])
        if m.get('msgType') is not None:
            self.msg_type = m.get('msgType')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class SendOfficialAccountSNSMessageRequest(TeaModel):
    def __init__(
        self,
        binding_token: str = None,
        biz_id: str = None,
        detail: SendOfficialAccountSNSMessageRequestDetail = None,
    ):
        self.binding_token = binding_token
        self.biz_id = biz_id
        self.detail = detail

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binding_token is not None:
            result['bindingToken'] = self.binding_token
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.detail is not None:
            result['detail'] = self.detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bindingToken') is not None:
            self.binding_token = m.get('bindingToken')
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('detail') is not None:
            temp_model = SendOfficialAccountSNSMessageRequestDetail()
            self.detail = temp_model.from_map(m['detail'])
        return self


class SendOfficialAccountSNSMessageResponseBodyResult(TeaModel):
    def __init__(
        self,
        open_push_id: str = None,
    ):
        self.open_push_id = open_push_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_push_id is not None:
            result['openPushId'] = self.open_push_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openPushId') is not None:
            self.open_push_id = m.get('openPushId')
        return self


class SendOfficialAccountSNSMessageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: SendOfficialAccountSNSMessageResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = SendOfficialAccountSNSMessageResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class SendOfficialAccountSNSMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendOfficialAccountSNSMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendOfficialAccountSNSMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ServiceWindowMessageBatchPushHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class ServiceWindowMessageBatchPushRequestDetailMessageBodyActionCardButtonList(TeaModel):
    def __init__(
        self,
        action_url: str = None,
        title: str = None,
    ):
        self.action_url = action_url
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_url is not None:
            result['actionUrl'] = self.action_url
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionUrl') is not None:
            self.action_url = m.get('actionUrl')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ServiceWindowMessageBatchPushRequestDetailMessageBodyActionCard(TeaModel):
    def __init__(
        self,
        button_list: List[ServiceWindowMessageBatchPushRequestDetailMessageBodyActionCardButtonList] = None,
        button_orientation: str = None,
        markdown: str = None,
        single_title: str = None,
        single_url: str = None,
        title: str = None,
    ):
        self.button_list = button_list
        self.button_orientation = button_orientation
        self.markdown = markdown
        self.single_title = single_title
        self.single_url = single_url
        self.title = title

    def validate(self):
        if self.button_list:
            for k in self.button_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['buttonList'] = []
        if self.button_list is not None:
            for k in self.button_list:
                result['buttonList'].append(k.to_map() if k else None)
        if self.button_orientation is not None:
            result['buttonOrientation'] = self.button_orientation
        if self.markdown is not None:
            result['markdown'] = self.markdown
        if self.single_title is not None:
            result['singleTitle'] = self.single_title
        if self.single_url is not None:
            result['singleUrl'] = self.single_url
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.button_list = []
        if m.get('buttonList') is not None:
            for k in m.get('buttonList'):
                temp_model = ServiceWindowMessageBatchPushRequestDetailMessageBodyActionCardButtonList()
                self.button_list.append(temp_model.from_map(k))
        if m.get('buttonOrientation') is not None:
            self.button_orientation = m.get('buttonOrientation')
        if m.get('markdown') is not None:
            self.markdown = m.get('markdown')
        if m.get('singleTitle') is not None:
            self.single_title = m.get('singleTitle')
        if m.get('singleUrl') is not None:
            self.single_url = m.get('singleUrl')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ServiceWindowMessageBatchPushRequestDetailMessageBodyLink(TeaModel):
    def __init__(
        self,
        message_url: str = None,
        pic_url: str = None,
        text: str = None,
        title: str = None,
    ):
        self.message_url = message_url
        self.pic_url = pic_url
        self.text = text
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_url is not None:
            result['messageUrl'] = self.message_url
        if self.pic_url is not None:
            result['picUrl'] = self.pic_url
        if self.text is not None:
            result['text'] = self.text
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('messageUrl') is not None:
            self.message_url = m.get('messageUrl')
        if m.get('picUrl') is not None:
            self.pic_url = m.get('picUrl')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ServiceWindowMessageBatchPushRequestDetailMessageBodyMarkdown(TeaModel):
    def __init__(
        self,
        text: str = None,
        title: str = None,
    ):
        self.text = text
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['text'] = self.text
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ServiceWindowMessageBatchPushRequestDetailMessageBodyText(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class ServiceWindowMessageBatchPushRequestDetailMessageBody(TeaModel):
    def __init__(
        self,
        action_card: ServiceWindowMessageBatchPushRequestDetailMessageBodyActionCard = None,
        link: ServiceWindowMessageBatchPushRequestDetailMessageBodyLink = None,
        markdown: ServiceWindowMessageBatchPushRequestDetailMessageBodyMarkdown = None,
        text: ServiceWindowMessageBatchPushRequestDetailMessageBodyText = None,
    ):
        self.action_card = action_card
        self.link = link
        self.markdown = markdown
        self.text = text

    def validate(self):
        if self.action_card:
            self.action_card.validate()
        if self.link:
            self.link.validate()
        if self.markdown:
            self.markdown.validate()
        if self.text:
            self.text.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_card is not None:
            result['actionCard'] = self.action_card.to_map()
        if self.link is not None:
            result['link'] = self.link.to_map()
        if self.markdown is not None:
            result['markdown'] = self.markdown.to_map()
        if self.text is not None:
            result['text'] = self.text.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionCard') is not None:
            temp_model = ServiceWindowMessageBatchPushRequestDetailMessageBodyActionCard()
            self.action_card = temp_model.from_map(m['actionCard'])
        if m.get('link') is not None:
            temp_model = ServiceWindowMessageBatchPushRequestDetailMessageBodyLink()
            self.link = temp_model.from_map(m['link'])
        if m.get('markdown') is not None:
            temp_model = ServiceWindowMessageBatchPushRequestDetailMessageBodyMarkdown()
            self.markdown = temp_model.from_map(m['markdown'])
        if m.get('text') is not None:
            temp_model = ServiceWindowMessageBatchPushRequestDetailMessageBodyText()
            self.text = temp_model.from_map(m['text'])
        return self


class ServiceWindowMessageBatchPushRequestDetail(TeaModel):
    def __init__(
        self,
        biz_request_id: str = None,
        message_body: ServiceWindowMessageBatchPushRequestDetailMessageBody = None,
        msg_type: str = None,
        send_to_all: bool = None,
        user_id_list: List[str] = None,
        uuid: str = None,
    ):
        self.biz_request_id = biz_request_id
        self.message_body = message_body
        self.msg_type = msg_type
        self.send_to_all = send_to_all
        self.user_id_list = user_id_list
        self.uuid = uuid

    def validate(self):
        if self.message_body:
            self.message_body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_request_id is not None:
            result['bizRequestId'] = self.biz_request_id
        if self.message_body is not None:
            result['messageBody'] = self.message_body.to_map()
        if self.msg_type is not None:
            result['msgType'] = self.msg_type
        if self.send_to_all is not None:
            result['sendToAll'] = self.send_to_all
        if self.user_id_list is not None:
            result['userIdList'] = self.user_id_list
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizRequestId') is not None:
            self.biz_request_id = m.get('bizRequestId')
        if m.get('messageBody') is not None:
            temp_model = ServiceWindowMessageBatchPushRequestDetailMessageBody()
            self.message_body = temp_model.from_map(m['messageBody'])
        if m.get('msgType') is not None:
            self.msg_type = m.get('msgType')
        if m.get('sendToAll') is not None:
            self.send_to_all = m.get('sendToAll')
        if m.get('userIdList') is not None:
            self.user_id_list = m.get('userIdList')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class ServiceWindowMessageBatchPushRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        detail: ServiceWindowMessageBatchPushRequestDetail = None,
    ):
        self.biz_id = biz_id
        self.detail = detail

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.detail is not None:
            result['detail'] = self.detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('detail') is not None:
            temp_model = ServiceWindowMessageBatchPushRequestDetail()
            self.detail = temp_model.from_map(m['detail'])
        return self


class ServiceWindowMessageBatchPushResponseBodyResult(TeaModel):
    def __init__(
        self,
        open_push_id: str = None,
    ):
        self.open_push_id = open_push_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_push_id is not None:
            result['openPushId'] = self.open_push_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openPushId') is not None:
            self.open_push_id = m.get('openPushId')
        return self


class ServiceWindowMessageBatchPushResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ServiceWindowMessageBatchPushResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ServiceWindowMessageBatchPushResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ServiceWindowMessageBatchPushResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ServiceWindowMessageBatchPushResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ServiceWindowMessageBatchPushResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCrmPersonalCustomerHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class UpdateCrmPersonalCustomerRequestPermission(TeaModel):
    def __init__(
        self,
        owner_staff_ids: List[str] = None,
        participant_staff_ids: List[str] = None,
    ):
        self.owner_staff_ids = owner_staff_ids
        self.participant_staff_ids = participant_staff_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_staff_ids is not None:
            result['ownerStaffIds'] = self.owner_staff_ids
        if self.participant_staff_ids is not None:
            result['participantStaffIds'] = self.participant_staff_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ownerStaffIds') is not None:
            self.owner_staff_ids = m.get('ownerStaffIds')
        if m.get('participantStaffIds') is not None:
            self.participant_staff_ids = m.get('participantStaffIds')
        return self


class UpdateCrmPersonalCustomerRequest(TeaModel):
    def __init__(
        self,
        action: str = None,
        data: Dict[str, Any] = None,
        extend_data: Dict[str, Any] = None,
        instance_id: str = None,
        modifier_nick: str = None,
        modifier_user_id: str = None,
        permission: UpdateCrmPersonalCustomerRequestPermission = None,
        relation_type: str = None,
        skip_duplicate_check: bool = None,
    ):
        self.action = action
        self.data = data
        self.extend_data = extend_data
        self.instance_id = instance_id
        self.modifier_nick = modifier_nick
        self.modifier_user_id = modifier_user_id
        self.permission = permission
        self.relation_type = relation_type
        self.skip_duplicate_check = skip_duplicate_check

    def validate(self):
        if self.permission:
            self.permission.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.data is not None:
            result['data'] = self.data
        if self.extend_data is not None:
            result['extendData'] = self.extend_data
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.modifier_nick is not None:
            result['modifierNick'] = self.modifier_nick
        if self.modifier_user_id is not None:
            result['modifierUserId'] = self.modifier_user_id
        if self.permission is not None:
            result['permission'] = self.permission.to_map()
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        if self.skip_duplicate_check is not None:
            result['skipDuplicateCheck'] = self.skip_duplicate_check
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('extendData') is not None:
            self.extend_data = m.get('extendData')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('modifierNick') is not None:
            self.modifier_nick = m.get('modifierNick')
        if m.get('modifierUserId') is not None:
            self.modifier_user_id = m.get('modifierUserId')
        if m.get('permission') is not None:
            temp_model = UpdateCrmPersonalCustomerRequestPermission()
            self.permission = temp_model.from_map(m['permission'])
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        if m.get('skipDuplicateCheck') is not None:
            self.skip_duplicate_check = m.get('skipDuplicateCheck')
        return self


class UpdateCrmPersonalCustomerResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class UpdateCrmPersonalCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCrmPersonalCustomerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCrmPersonalCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupSetHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class UpdateGroupSetRequest(TeaModel):
    def __init__(
        self,
        manager_user_ids: str = None,
        member_quota: int = None,
        name: str = None,
        notice: str = None,
        notice_toped: int = None,
        open_group_set_id: str = None,
        owner_user_id: str = None,
        template_id: str = None,
        welcome: str = None,
    ):
        self.manager_user_ids = manager_user_ids
        self.member_quota = member_quota
        self.name = name
        self.notice = notice
        self.notice_toped = notice_toped
        self.open_group_set_id = open_group_set_id
        self.owner_user_id = owner_user_id
        self.template_id = template_id
        self.welcome = welcome

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager_user_ids is not None:
            result['managerUserIds'] = self.manager_user_ids
        if self.member_quota is not None:
            result['memberQuota'] = self.member_quota
        if self.name is not None:
            result['name'] = self.name
        if self.notice is not None:
            result['notice'] = self.notice
        if self.notice_toped is not None:
            result['noticeToped'] = self.notice_toped
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.owner_user_id is not None:
            result['ownerUserId'] = self.owner_user_id
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.welcome is not None:
            result['welcome'] = self.welcome
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('managerUserIds') is not None:
            self.manager_user_ids = m.get('managerUserIds')
        if m.get('memberQuota') is not None:
            self.member_quota = m.get('memberQuota')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('notice') is not None:
            self.notice = m.get('notice')
        if m.get('noticeToped') is not None:
            self.notice_toped = m.get('noticeToped')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('ownerUserId') is not None:
            self.owner_user_id = m.get('ownerUserId')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('welcome') is not None:
            self.welcome = m.get('welcome')
        return self


class UpdateGroupSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: bool = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class UpdateRelationMetaFieldHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class UpdateRelationMetaFieldRequestFieldDTOListPropsOptions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateRelationMetaFieldRequestFieldDTOListProps(TeaModel):
    def __init__(
        self,
        align: str = None,
        biz_alias: str = None,
        choice: int = None,
        content: str = None,
        disabled: bool = None,
        duration: bool = None,
        field_id: str = None,
        format: str = None,
        invisible: bool = None,
        label: str = None,
        label_editable_freeze: bool = None,
        link: str = None,
        need_detail: str = None,
        not_print: str = None,
        not_upper: str = None,
        options: List[UpdateRelationMetaFieldRequestFieldDTOListPropsOptions] = None,
        pay_enable: bool = None,
        placeholder: str = None,
        required: bool = None,
        required_editable_freeze: bool = None,
        sortable: bool = None,
        unit: str = None,
    ):
        self.align = align
        self.biz_alias = biz_alias
        self.choice = choice
        self.content = content
        self.disabled = disabled
        self.duration = duration
        self.field_id = field_id
        self.format = format
        self.invisible = invisible
        self.label = label
        self.label_editable_freeze = label_editable_freeze
        self.link = link
        self.need_detail = need_detail
        self.not_print = not_print
        self.not_upper = not_upper
        self.options = options
        self.pay_enable = pay_enable
        self.placeholder = placeholder
        self.required = required
        self.required_editable_freeze = required_editable_freeze
        self.sortable = sortable
        self.unit = unit

    def validate(self):
        if self.options:
            for k in self.options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align is not None:
            result['align'] = self.align
        if self.biz_alias is not None:
            result['bizAlias'] = self.biz_alias
        if self.choice is not None:
            result['choice'] = self.choice
        if self.content is not None:
            result['content'] = self.content
        if self.disabled is not None:
            result['disabled'] = self.disabled
        if self.duration is not None:
            result['duration'] = self.duration
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.format is not None:
            result['format'] = self.format
        if self.invisible is not None:
            result['invisible'] = self.invisible
        if self.label is not None:
            result['label'] = self.label
        if self.label_editable_freeze is not None:
            result['labelEditableFreeze'] = self.label_editable_freeze
        if self.link is not None:
            result['link'] = self.link
        if self.need_detail is not None:
            result['needDetail'] = self.need_detail
        if self.not_print is not None:
            result['notPrint'] = self.not_print
        if self.not_upper is not None:
            result['notUpper'] = self.not_upper
        result['options'] = []
        if self.options is not None:
            for k in self.options:
                result['options'].append(k.to_map() if k else None)
        if self.pay_enable is not None:
            result['payEnable'] = self.pay_enable
        if self.placeholder is not None:
            result['placeholder'] = self.placeholder
        if self.required is not None:
            result['required'] = self.required
        if self.required_editable_freeze is not None:
            result['requiredEditableFreeze'] = self.required_editable_freeze
        if self.sortable is not None:
            result['sortable'] = self.sortable
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('align') is not None:
            self.align = m.get('align')
        if m.get('bizAlias') is not None:
            self.biz_alias = m.get('bizAlias')
        if m.get('choice') is not None:
            self.choice = m.get('choice')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('invisible') is not None:
            self.invisible = m.get('invisible')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('labelEditableFreeze') is not None:
            self.label_editable_freeze = m.get('labelEditableFreeze')
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('needDetail') is not None:
            self.need_detail = m.get('needDetail')
        if m.get('notPrint') is not None:
            self.not_print = m.get('notPrint')
        if m.get('notUpper') is not None:
            self.not_upper = m.get('notUpper')
        self.options = []
        if m.get('options') is not None:
            for k in m.get('options'):
                temp_model = UpdateRelationMetaFieldRequestFieldDTOListPropsOptions()
                self.options.append(temp_model.from_map(k))
        if m.get('payEnable') is not None:
            self.pay_enable = m.get('payEnable')
        if m.get('placeholder') is not None:
            self.placeholder = m.get('placeholder')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('requiredEditableFreeze') is not None:
            self.required_editable_freeze = m.get('requiredEditableFreeze')
        if m.get('sortable') is not None:
            self.sortable = m.get('sortable')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class UpdateRelationMetaFieldRequestFieldDTOList(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        props: UpdateRelationMetaFieldRequestFieldDTOListProps = None,
    ):
        self.component_name = component_name
        self.props = props

    def validate(self):
        if self.props:
            self.props.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.props is not None:
            result['props'] = self.props.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('props') is not None:
            temp_model = UpdateRelationMetaFieldRequestFieldDTOListProps()
            self.props = temp_model.from_map(m['props'])
        return self


class UpdateRelationMetaFieldRequest(TeaModel):
    def __init__(
        self,
        field_dtolist: List[UpdateRelationMetaFieldRequestFieldDTOList] = None,
        operator_user_id: str = None,
        relation_type: str = None,
        tenant: str = None,
    ):
        self.field_dtolist = field_dtolist
        self.operator_user_id = operator_user_id
        self.relation_type = relation_type
        self.tenant = tenant

    def validate(self):
        if self.field_dtolist:
            for k in self.field_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['fieldDTOList'] = []
        if self.field_dtolist is not None:
            for k in self.field_dtolist:
                result['fieldDTOList'].append(k.to_map() if k else None)
        if self.operator_user_id is not None:
            result['operatorUserId'] = self.operator_user_id
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        if self.tenant is not None:
            result['tenant'] = self.tenant
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.field_dtolist = []
        if m.get('fieldDTOList') is not None:
            for k in m.get('fieldDTOList'):
                temp_model = UpdateRelationMetaFieldRequestFieldDTOList()
                self.field_dtolist.append(temp_model.from_map(k))
        if m.get('operatorUserId') is not None:
            self.operator_user_id = m.get('operatorUserId')
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        if m.get('tenant') is not None:
            self.tenant = m.get('tenant')
        return self


class UpdateRelationMetaFieldResponseBody(TeaModel):
    def __init__(
        self,
        relation_type: str = None,
    ):
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
        return self


class UpdateRelationMetaFieldResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRelationMetaFieldResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRelationMetaFieldResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


