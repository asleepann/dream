import functools
import logging
import random
from typing import Any, Callable, Optional, Iterator

from common.dff.integration.processing import save_slots_to_ctx
from scenario.condition import get_current_dessert_name, graph
from df_engine.core import Context, Actor

logger = logging.getLogger(__name__)

# ....


def fill_responses_by_slots_from_graph(entity):
    def fill_responses_by_slots_processing(
        ctx: Context,
        actor: Actor,
        *args,
        **kwargs,
    ) -> Context:
        processed_node = ctx.a_s.get("processed_node", ctx.a_s["next_node"])
        slot_value = []
        dessert_id = get_current_dessert_name(ctx, actor)
        if dessert_id:
            dessert_id = dessert_id.replace(" ", "_")
            current_dessert_id = dessert_id.capitalize()
        ingredients = graph.ontology.get_entity_kind(current_dessert_id)
        for k, v in ingredients.items():
            if isinstance(v, dict):
                slot_value.append(v["@class"])
        slot_value = ", ".join(slot_value)
        processed_node.response = processed_node.response.replace("{" f"{entity}" "}", slot_value)
        ctx.a_s["processed_node"] = processed_node
        return ctx

    return fill_responses_by_slots_processing