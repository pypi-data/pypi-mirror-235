import click

from CveXplore.cli_cmds.cli_utils.utils import printer
from CveXplore.cli_cmds.mutex_options.mutex import Mutex


@click.group("cve", invoke_without_command=True, help="Query for cve specific data")
@click.pass_context
def cve_cmd(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(cve_cmd.get_help(ctx))


@cve_cmd.group(
    "search",
    invoke_without_command=True,
    help="Search for cve entries by id",
)
@click.option(
    "-c",
    "--cve",
    help="Search for CVE's (could be multiple)",
    multiple=True,
    cls=Mutex,
    not_required_if=["field_list"],
)
@click.option(
    "-f",
    "--field",
    help="Field to return (could be multiple)",
    multiple=True,
    cls=Mutex,
    not_required_if=["field_list"],
)
@click.option(
    "-fl",
    "--field_list",
    help="Return a field list for this collection",
    multiple=True,
    is_flag=True,
    cls=Mutex,
    not_required_if=["field", "cve"],
)
@click.option(
    "-o",
    "--output",
    default="json",
    help="Set the desired output format (defaults to json)",
    type=click.Choice(["json", "csv", "xml", "html"], case_sensitive=False),
)
@click.pass_context
def search_cmd(
    ctx,
    cve,
    field,
    field_list,
    output,
):
    if cve:
        ret_list = getattr(ctx.obj["data_source"], "cves").mget_by_id(*cve)
    elif field_list:
        ret_list = getattr(ctx.obj["data_source"], "cves").field_list()
    else:
        click.echo(search_cmd.get_help(ctx))
        return

    if isinstance(ret_list, list):
        result = [result.to_dict(*field) for result in ret_list]
    elif isinstance(ret_list, set):
        result = sorted([result for result in ret_list])
    else:
        result = []

    if ctx.invoked_subcommand is None:
        printer(input_data=result, output=output)
    else:
        ctx.obj["RESULT"] = result


@cve_cmd.group(
    "last",
    invoke_without_command=True,
    help="Query the last L (-l) amount of cve entries",
)
@click.option("-l", "--limit", default=10, help="Query limit")
@click.option(
    "-o",
    "--output",
    default="json",
    help="Set the desired output format (defaults to json)",
    type=click.Choice(["json", "csv", "xml", "html"], case_sensitive=False),
)
@click.pass_context
def last_cmd(ctx, limit, output):
    ret_list = ctx.obj["data_source"].last_cves(limit=limit)

    result = [result.to_dict() for result in ret_list]

    if ctx.invoked_subcommand is None:
        printer(input_data=result, output=output)
    else:
        ctx.obj["RESULT"] = result
