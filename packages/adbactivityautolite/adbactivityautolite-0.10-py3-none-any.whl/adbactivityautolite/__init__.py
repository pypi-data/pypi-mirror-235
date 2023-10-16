import re
import sys
import time

import regex
from usefuladb import AdbCommands
from a_pandas_ex_apply_ignore_exceptions import pd_add_apply_ignore_exceptions
import pandas as pd

pd_add_apply_ignore_exceptions()
from a_pandas_ex_less_memory_more_speed import pd_add_less_memory_more_speed

pd_add_less_memory_more_speed()
import numpy as np

methods_to_add = [
    "sh_input_dpad_longtap",
    "sh_input_dpad_tap",
    "sh_input_gamepad_longtap",
    "sh_input_gamepad_tap",
    "sh_input_joystick_longtap",
    "sh_input_joystick_tap",
    "sh_input_keyboard_longtap",
    "sh_input_keyboard_tap",
    "sh_input_mouse_longtap",
    "sh_input_mouse_tap",
    "sh_input_stylus_longtap",
    "sh_input_stylus_tap",
    "sh_input_tap",
    "sh_input_touchnavigation_longtap",
    "sh_input_touchnavigation_tap",
    "sh_input_touchpad_longtap",
    "sh_input_touchpad_tap",
    "sh_input_touchscreen_longtap",
    "sh_input_touchscreen_tap",
    "sh_input_trackball_longtap",
    "sh_input_trackball_tap",
]
top_activity_command = "dumpsys activity top -c"
view_hierachy_regex = re.compile(r"^\s*(View Hierarchy):\s*$")
looper_regex = re.compile(r"^\s*Looper.*\}\s*$")

gesklammer2 = re.compile(
    r"^\s+([^{]+)",
    flags=re.I,
)
spacesbeg = regex.compile(
    r"^(\s+)",
    flags=regex.I,
)
spacesbegre = re.compile(
    r"^(\s+)",
    flags=regex.I,
)

dfindetails = re.compile(
    r"^\s+[^{]+\{([^\}]+)",
    flags=regex.I,
)
widgetreg = re.compile(
    r"^(-?\d+),(-?\d+)-?(-?\d+),(-?\d+)",
    flags=regex.I,
)
detailregex = regex.compile(r"^detail_[^0]\d*$")
aabeginning = regex.compile("^aa_")
spacebeginningcounter = re.compile(r"^\s+", flags=re.I)


class ParentGetter:
    def __init__(self, dfra, ind, activity_index):
        self.dfra = dfra
        self.ind = ind
        self.activity_index = activity_index

    def __repr__(self):
        return f"loc: {self.ind}"

    def __str__(self):
        return f"loc: {self.ind}"

    def __call__(self, *args, **kwargs):
        dfra = self.dfra()
        dfra3 = dfra.loc[dfra.aa_activity_index == self.activity_index]
        try:
            return _execute_function_to_df_show_parents(dfra3, dfra3.loc[self.ind])
        except Exception as e:
            sys.stderr.write(f"{e}\n")
            return pd.DataFrame()


class Tap:
    def __init__(self, fu, x, y, use_time=True, t=1):
        self.x = x
        self.y = y
        self.px = str(x).rjust(4)
        self.py = str(y).rjust(4)
        self.t = t
        self.use_time = use_time
        self.fu = fu

    def __str__(self):
        if self.use_time:
            return f"x:{self.px} y:{self.py} t:{self.t}"
        else:
            return f"x:{self.px} y:{self.py}"

    def __repr__(self):
        return self.__str__()

    def __call__(self, *args, **kwargs):
        ti = None
        if self.use_time:
            ti = args[0] if args else self.t
        try:
            if ti:
                return self.fu(self.x, self.y, ti)
            else:
                return self.fu(self.x, self.y)
        except Exception:
            return None, None


def get_detailed_info_sep(df):
    detailedinformationtogether = df.hiera.str.extractall(dfindetails).reset_index(
        drop=True
    )
    detailedinformationsep = detailedinformationtogether[0].str.split(
        n=5, regex=False, expand=True
    )  # .copy()
    detailedinformationsep.loc[:, 1] = detailedinformationsep[1].ds_apply_ignore(
        pd.NA, lambda x: (str(x).replace("None", "") + "..........")[:9]
    )
    detailedinformationsep.loc[:, 2] = detailedinformationsep[2].ds_apply_ignore(
        pd.NA, lambda x: (str(x).replace("None", "") + "..........")[:8]
    )

    return detailedinformationsep


def get_widget_coords(detailedinformationsep):
    return (
        detailedinformationsep[3]
        .str.strip()
        .str.extractall(widgetreg)
        .reset_index(drop=True)
        .astype("string")
        .astype("Int64")
        .rename(columns={0: "x_start", 1: "y_start", 2: "x_end", 3: "y_end"})
    )


def concat_df_widget_coords(df, widgetcoords):
    df = pd.concat([df, widgetcoords], axis=1)  # @#.copy()
    df.columns = [
        "aa_complete_dump",
        "aa_depth",
        "aa_class_name",
        "aa_x_start",
        "aa_y_start",
        "aa_x_end",
        "aa_y_end",
    ]
    return df


def concat_df_details(df, details):
    return pd.concat([df, details], axis=1)  # .copy()
    # return df


def get_details(detailedinformationsep):
    details = (detailedinformationsep[1] + detailedinformationsep[2]).ds_apply_ignore(
        pd.NA, lambda x: pd.Series(list(x))
    )
    details.replace({".": False}, inplace=True)
    for col in details.columns[1:]:
        details.loc[(details[col].astype("string").str.len() == 1), col] = True
    flacol = [
        "visibility",
        "focusable",
        "enabled",
        "drawn",
        "scrollbars_horizontal",
        "scrollbars_vertical",
        "clickable",
        "long_clickable",
        "context_clickable",
        "pflag_is_root_namespace",
        "pflag_focused",
        "pflag_selected",
        "pflag_prepressed",
        "pflag_hovered",
        "pflag_activated",
        "pflag_invalidated",
        "pflag_dirty_mask",
    ]
    details.columns = flacol
    return details


def calculate_center(df):
    df.loc[:, "aa_width"] = df["aa_x_end"] - df["aa_x_start"]
    df.loc[:, "aa_height"] = df["aa_y_end"] - df["aa_y_start"]
    df.loc[:, "aa_center_x"] = df["aa_x_start"] + (df["aa_width"] // 2)
    df.loc[:, "aa_center_y"] = df["aa_y_start"] + (df["aa_height"] // 2)
    df.loc[:, "aa_area"] = df["aa_width"] * df["aa_height"]
    return df


def get_label(va):
    try:
        stripped = va.strip("#")
        return pd.Series([stripped, int(stripped, base=16)])
    except Exception:
        return pd.Series([pd.NA, pd.NA])


def get_label_1(va):
    try:
        stripped = va.strip("#")
        return int(stripped, base=16)
    except Exception:
        return pd.NA


def hashcodes_ids_to_int(df, detailedinformationsep):
    int1 = detailedinformationsep[0].map(lambda x: get_label_1(x))

    int1hex = pd.concat(
        [int1, detailedinformationsep[0]], axis=1, ignore_index=True
    ).rename(columns={0: "aa_hashcode_int", 1: "aa_hashcode_hex"})

    return pd.concat(
        [
            pd.concat([df, int1hex], axis=1),
            (
                detailedinformationsep[4]
                .ds_apply_ignore(pd.NA, get_label)
                .rename(columns={0: "aa_mID_hex", 1: "aa_mID_int"})
            ),
        ],
        axis=1,
    )


def fill_missing_ids_with_na(df, detailedinformationsep):
    return pd.concat([df, detailedinformationsep[5].fillna(pd.NA)], axis=1).rename(
        columns={5: "aa_id_information"}
    )


def remove_spaces(df):
    spaces = df["aa_complete_dump"].str.extract(spacesbegre)[0]
    abslen = spaces.str.len().min()
    df.loc[:, "aa_complete_dump"] = df["aa_complete_dump"].str.slice(abslen)
    pureid = (
        df["aa_id_information"]
        .fillna("")
        .str.split(":")
        .ds_apply_ignore(pd.NA, lambda x: x[1] if len(x) == 2 else pd.NA)
    )
    df.loc[pureid.index, "pure_id"] = pureid.__array__().copy()
    for col_ in [x for x in df.columns if detailregex.search(str(x))]:
        df.loc[~df[col_].isna(), col_] = True
        df.loc[df[col_].isna(), col_] = False
    df.columns = ["aa_" + aabeginning.sub("", y) for y in df.columns.to_list()[:-1]] + [
        df.columns.to_list()[-1]
    ]
    return df


def reset_index_and_backup(df):
    df["old_index"] = df.index.__array__().copy()
    return df.reset_index(drop=True)


def get_all_children(df):
    cropcoords = []
    group2 = df.copy()
    alldepths = group2.aa_depth.unique().tolist()
    alldepths = list(reversed(sorted(alldepths)))
    for ini, depth in enumerate(alldepths):
        subgroup = group2.loc[group2.aa_depth == depth]
        for key, item in subgroup.iterrows():
            oldrunvalue = depth
            goodstuff = []
            for ra in reversed(range(0, key)):
                if df.at[ra, "aa_depth"] < oldrunvalue:
                    goodstuff.append(df.loc[ra].to_frame().T)

                    oldrunvalue = df.at[ra, "aa_depth"]
            try:
                subdf = pd.concat(goodstuff)
            except Exception as fe:
                continue

            singleitem = item.to_frame().T

            x00 = subdf.aa_x_start.sum() + item.aa_x_start
            y00 = subdf.aa_y_start.sum() + item.aa_y_start
            x01 = subdf.aa_x_start.sum() + item.aa_x_end
            y01 = subdf.aa_y_start.sum() + item.aa_y_end

            singleitem.loc[:, "aa_x_start_relative"] = singleitem.loc[:, "aa_x_start"]
            singleitem.loc[:, "aa_y_start_relative"] = singleitem.loc[:, "aa_y_start"]
            singleitem.loc[:, "aa_x_end_relative"] = singleitem.loc[:, "aa_x_end"]
            singleitem.loc[:, "aa_y_end_relative"] = singleitem.loc[:, "aa_y_end"]

            singleitem.loc[:, "aa_x_start"] = x00
            singleitem.loc[:, "aa_y_start"] = y00
            singleitem.loc[:, "aa_x_end"] = x01
            singleitem.loc[:, "aa_y_end"] = y01
            singleitem.loc[:, "aa_width"] = (
                singleitem["aa_x_end"] - singleitem["aa_x_start"]
            )
            singleitem.loc[:, "aa_height"] = (
                singleitem["aa_y_end"] - singleitem["aa_y_start"]
            )
            singleitem.loc[:, "aa_center_x"] = singleitem["aa_x_start"] + (
                singleitem["aa_width"] // 2
            )
            singleitem.loc[:, "aa_center_y"] = singleitem["aa_y_start"] + (
                singleitem["aa_height"] // 2
            )
            singleitem.loc[:, "aa_is_child"] = True

            for ini_pa, pa_id in enumerate(subdf.old_index):
                singleitem.loc[:, f"parent_{str(ini_pa).zfill(3)}"] = pa_id
            cropcoords.append(singleitem)
    return pd.concat(cropcoords).reset_index(drop=True)


def add_bounds_to_df(df):
    df["aa_bounds"] = df.apply(
        lambda x: tuple(
            (x["aa_x_start"], x["aa_y_start"], x["aa_x_end"], x["aa_y_end"])
        ),
        axis=1,
    )
    return df


def get_cropped_coords(max_x, max_y, df, pref="aa"):
    # pref = 'aa'
    df[f"{pref}_cropped_x_start"] = df[f"{pref}_x_start"]
    df[f"{pref}_cropped_y_start"] = df[f"{pref}_y_start"]
    df[f"{pref}_cropped_x_end"] = df[f"{pref}_x_end"]
    df[f"{pref}_cropped_y_end"] = df[f"{pref}_y_end"]

    df.loc[(df[f"{pref}_cropped_x_start"] <= 0), f"{pref}_cropped_x_start"] = 0
    df.loc[(df[f"{pref}_cropped_y_start"] <= 0), f"{pref}_cropped_y_start"] = 0
    df.loc[(df[f"{pref}_cropped_x_end"] <= 0), f"{pref}_cropped_x_end"] = 0
    df.loc[(df[f"{pref}_cropped_y_end"] <= 0), f"{pref}_cropped_y_end"] = 0

    df.loc[(df[f"{pref}_cropped_x_start"] >= max_x), f"{pref}_cropped_x_start"] = max_x
    df.loc[(df[f"{pref}_cropped_y_start"] >= max_y), f"{pref}_cropped_y_start"] = max_y
    df.loc[(df[f"{pref}_cropped_x_end"] >= max_x), f"{pref}_cropped_x_end"] = max_x
    df.loc[(df[f"{pref}_cropped_y_end"] >= max_y), f"{pref}_cropped_y_end"] = max_y
    df.loc[:, f"{pref}_width_cropped"] = (
        df[f"{pref}_cropped_x_end"] - df[f"{pref}_cropped_x_start"]
    )
    df.loc[:, f"{pref}_height_cropped"] = (
        df[f"{pref}_cropped_y_end"] - df[f"{pref}_cropped_y_start"]
    )
    df.loc[:, f"{pref}_center_x_cropped"] = df[f"{pref}_cropped_x_start"] + (
        df[f"{pref}_width_cropped"] // 2
    )
    df.loc[:, f"{pref}_center_y_cropped"] = df[f"{pref}_cropped_y_start"] + (
        df[f"{pref}_height_cropped"] // 2
    )
    return df


def optimize_dtypes(df, ignore_columns):
    return df.ds_reduce_memory_size_carefully(
        ignore_columns=ignore_columns, verbose=False
    )


def cut_spaces(df):
    try:
        if (
            g := df.aa_complete_dump.str.findall(spacebeginningcounter)
            .str[0]
            .str.len()
            .min()
            > 0
        ):
            df.loc[:, "aa_complete_dump"] = df.aa_complete_dump.str.slice(start=g)
    except Exception:
        pass
    df.loc[:, "aa_complete_dump"] = df.aa_complete_dump.str.rstrip()
    return df


def _execute_function_to_df_show_parents(df, item):
    itemf = item.to_frame().T.dropna(axis=1)

    sortedcols = [
        x
        for x in list(reversed(sorted(itemf.columns.to_list())))
        if str(x).startswith("parent_")
    ]
    allparentscols = [
        df.loc[df.aa_old_index == int(itemf[x])]
        for x in sortedcols
        if str(x).startswith("parent")
    ]
    return pd.concat(allparentscols).sort_values(by="aa_depth", ascending=False)


def format_df(dfax2):
    df = dfax2.drop(columns=["aa_tmp"]).copy()
    df.columns = ["hiera"]
    spaces = df.hiera.ds_apply_ignore(pd.NA, lambda q: spacesbeg.findall(q)[0])
    abslen = spaces.str.len()
    abslenwithoutmen = abslen - abslen.min()
    level = abslenwithoutmen // 2
    df = pd.concat([df, level], ignore_index=True, axis=1)
    df.columns = ["hiera", "level"]
    return df


def get_uiactivitydf(
    adbdev,
    h,
    w,
    timeout=60,
    with_fu=True,
    t_long_touch=1,
    better_dtypes=True,
    **kwargs,
):
    def _gfa():
        kwargs.update({"print_stdout": False})
        df = pd.DataFrame(
            [
                q.decode("utf-8", "backslashreplace").rstrip()
                for q in adbdev.execute_sh_command(top_activity_command, **kwargs)[0]
            ]
        )
        df.columns = ["aa_data"]
        df["aa_tmp"] = df.aa_data.str.extract(view_hierachy_regex)
        alldfs = np.array_split(df, df.dropna(subset="aa_tmp").index)
        firstclean = []
        counter = 0
        for dfax in alldfs:
            try:
                dfax2 = dfax.loc[
                    dfax.aa_data.str.extractall(dfindetails).reset_index(drop=False)[
                        "level_0"
                    ]
                ].reset_index(drop=True)
                spli = np.array_split(
                    dfax2, dfax2.loc[dfax2.aa_data.str.contains(looper_regex)].index
                )[0]
                spli = spli.assign(hiera=spli.aa_data).drop(columns=["aa_data"])
                spliinfo = get_detailed_info_sep(spli)
                fomspli = format_df(spli)
                wico = get_widget_coords(spliinfo)
                fomspli.loc[:, "aa_class_name"] = fomspli.hiera.str.extractall(
                    gesklammer2
                ).reset_index(drop=True)
                cowico = concat_df_widget_coords(fomspli, wico)
                alldet = get_details(spliinfo)
                df2xx = reset_index_and_backup(
                    remove_spaces(
                        fill_missing_ids_with_na(
                            hashcodes_ids_to_int(
                                calculate_center(concat_df_details(cowico, alldet)),
                                spliinfo,
                            ),
                            spliinfo,
                        )
                    )
                )
                df2xx = cut_spaces(
                    get_cropped_coords(
                        h,
                        w,
                        add_bounds_to_df(get_all_children(df=df2xx)).rename(
                            columns={
                                "pure_id": "aa_pure_id",
                                "old_index": "aa_old_index",
                            }
                        ),
                        pref="aa",
                    )
                )
                df2xx = df2xx.reset_index(drop=True)
                df2xx = df2xx.assign(
                    aa_activity_index=counter,
                    aa_activity_id=df2xx.index.__array__().copy(),
                )
                if better_dtypes:
                    df2xx = optimize_dtypes(
                        df2xx,
                        ignore_columns=[
                            x for x in df2xx.columns if not str(x).startswith("parent_")
                        ],
                    ).astype(
                        {
                            k: "Int64"
                            for k in df2xx.columns
                            if str(k).startswith("parent_")
                        }
                    )
                if with_fu:
                    for m in methods_to_add:
                        m_co = "ff_" + m[9:]
                        df2xx.loc[:, m_co] = df2xx.ds_apply_ignore(
                            pd.NA,
                            lambda q: Tap(
                                getattr(adbdev, m),
                                q.aa_center_x_cropped,
                                q.aa_center_y_cropped,
                                True if m_co.endswith("_longtap") else False,
                                t_long_touch,
                            ),
                            axis=1,
                        )
                df2xx["aa_get_parents"] = df2xx.apply(
                    lambda f: ParentGetter(
                        lambda: df2xx, ind=f.name, activity_index=f["aa_activity_index"]
                    ),
                    axis=1,
                )
                firstclean.append(df2xx)
                counter += 1

            except Exception as e:
                pass

        return pd.concat(firstclean)

    finaltimeout = time.time() + timeout
    while time.time() < finaltimeout:
        try:
            df2xxx = _gfa()
            return df2xxx[sorted(df2xxx.columns)]
        except Exception as fe:
            sys.stderr.write(f"{fe}\n")
    return pd.DataFrame()


class UiActivityDumpLite:
    def __init__(self, adb=None, adb_path=None, serial_number=None, **kwargs):
        if not adb:
            self.adb = AdbCommands(adb_path, serial_number, **kwargs)
        else:
            self.adb = adb
        self.w, self.h = None, None

    def __str__(self):
        return self.adb.device_serial

    def __repr__(self):
        return self.adb.device_serial

    def update_width_height(self, **kwargs):
        kwargsdict = kwargs.copy()
        kwargsdict.update({"print_stdout": False})

        self.w, self.h = self.adb.sh_get_resolution(print_stdout=False)

    def get_df(
        self,
        timeout=60,
        with_fu=True,
        t_long_touch=1,
        better_dtypes=True,
        **kwargs,
    ):
        return get_uiactivitydf(
            self.adb,
            h=self.h,
            w=self.w,
            timeout=timeout,
            with_fu=with_fu,
            t_long_touch=t_long_touch,
            better_dtypes=better_dtypes,
            **kwargs,
        )


