from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

example_url = "https://maini-game.com.cn"
default_keyword = "爱游戏"


@dataclass
class KeywordNote:
    keyword: str
    url: str
    content: str
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    def __post_init__(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if self.created_at is None:
            self.created_at = now
        if self.updated_at is None:
            self.updated_at = now
        self.updated_at = now


def format_note_brief(note: KeywordNote) -> str:
    tags_str = ", ".join(note.tags) if note.tags else "无标签"
    return (
        f"[{note.keyword}] {note.content[:40]}... "
        f"| 标签: {tags_str} | 更新: {note.updated_at}"
    )


def format_note_full(note: KeywordNote) -> str:
    header = f"关键词: {note.keyword}\n关联链接: {note.url}\n内容: {note.content}"
    tags_section = f"标签: {', '.join(note.tags) if note.tags else '无'}"
    time_section = f"创建时间: {note.created_at}\n更新时间: {note.updated_at}"
    sep = "-" * 40
    return f"{header}\n{tags_section}\n{time_section}\n{sep}"


def export_to_markdown(notes: List[KeywordNote], filepath: str = "notes_export.md") -> None:
    lines = ["# 关键词笔记导出\n"]
    for idx, note in enumerate(notes, 1):
        lines.append(f"## {idx}. {note.keyword}\n")
        lines.append(f"- **关键词**: {note.keyword}")
        lines.append(f"- **URL**: {note.url}")
        lines.append(f"- **内容**: {note.content}")
        lines.append(f"- **标签**: {', '.join(note.tags) if note.tags else '无'}")
        lines.append(f"- **创建**: {note.created_at}")
        lines.append(f"- **更新**: {note.updated_at}")
        lines.append("")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def build_sample_notes() -> List[KeywordNote]:
    return [
        KeywordNote(
            keyword="爱游戏",
            url=example_url,
            content="这是一个关于爱游戏的笔记示例，展示基础用法与结构。",
            tags=["游戏", "娱乐", "示例"],
        ),
        KeywordNote(
            keyword="爱游戏",
            url=example_url,
            content="爱游戏平台提供多种在线娱乐内容，用户反馈积极。",
            tags=["游戏", "平台"],
        ),
        KeywordNote(
            keyword="爱游戏",
            url=example_url,
            content="爱游戏社区聚集了大量玩家，讨论攻略与心得。",
            tags=["社区", "玩家", "分享"],
        ),
    ]


def main():
    notes = build_sample_notes()
    print("=== 简要格式 ===")
    for note in notes:
        print(format_note_brief(note))
    print("\n=== 完整格式 ===")
    for note in notes:
        print(format_note_full(note))
    export_to_markdown(notes, "keyword_notes_export.md")
    print("\n笔记已导出至 keyword_notes_export.md")


if __name__ == "__main__":
    main()