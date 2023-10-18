from .. import context
from ..input_helpers import (
    get_org_from_input_or_ctx,
    strip_none,
    build_updated_model_validate,
)
import agilicus
from ..output.table import (
    spec_column,
    format_table,
    metadata_column,
)


def add_label(ctx, name, **kwargs):
    token = context.get_token(ctx)
    apiclient = context.get_apiclient(ctx, token)
    kwargs["org_id"] = get_org_from_input_or_ctx(ctx, **kwargs)
    kwargs = strip_none(kwargs)

    spec = agilicus.LabelSpec(name=agilicus.LabelName(name), **kwargs)

    label = agilicus.Label(spec=spec)
    return apiclient.labels_api.create_object_label(label).to_dict()


def list_labels(ctx, name, **kwargs):
    token = context.get_token(ctx)
    apiclient = context.get_apiclient(ctx, token)
    kwargs["org_id"] = get_org_from_input_or_ctx(ctx, **kwargs)
    kwargs = strip_none(kwargs)
    if name is not None:
        kwargs["label_name"] = agilicus.LabelName(name)

    return apiclient.labels_api.list_object_labels(**kwargs).labels


def get_label(ctx, **kwargs):
    token = context.get_token(ctx)
    apiclient = context.get_apiclient(ctx, token)
    kwargs["org_id"] = get_org_from_input_or_ctx(ctx, **kwargs)
    kwargs = strip_none(kwargs)

    return apiclient.labels_api.get_object_label(**kwargs)


def delete_label(ctx, **kwargs):
    token = context.get_token(ctx)
    apiclient = context.get_apiclient(ctx, token)
    kwargs["org_id"] = get_org_from_input_or_ctx(ctx, **kwargs)
    kwargs = strip_none(kwargs)

    apiclient.labels_api.delete_object_label(**kwargs)


def replace_label(ctx, label_id, org_id, **kwargs):
    token = context.get_token(ctx)
    apiclient = context.get_apiclient(ctx, token)
    org_id = get_org_from_input_or_ctx(ctx, org_id=org_id)
    kwargs = strip_none(kwargs)

    label = apiclient.labels_api.get_object_label(label_id=label_id, org_id=org_id)
    kwargs["org_id"] = org_id

    label.spec = build_updated_model_validate(
        agilicus.LabelSpec,
        label,
        kwargs,
        True,
    )

    return apiclient.labels_api.replace_object_label(label_id, label=label)


def format_labels(ctx, labels):
    columns = [
        metadata_column("id"),
        spec_column("org_id"),
        spec_column("name"),
        spec_column("description"),
    ]

    return format_table(ctx, labels, columns)


def add_labelled_object(ctx, **kwargs):
    raise Exception("not implemented")


def list_labelled_objects(ctx, **kwargs):
    raise Exception("not implemented")


def get_labelled_object(ctx, **kwargs):
    raise Exception("not implemented")


def delete_labelled_object(ctx, **kwargs):
    raise Exception("not implemented")


def replace_labelled_object(ctx, **kwargs):
    raise Exception("not implemented")


def format_labelled_objects(ctx, *args):
    raise Exception("not implemented")
