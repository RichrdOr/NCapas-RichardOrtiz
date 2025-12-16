from django.contrib import admin
from .models import (
    Deporte,
    Evento,
    Participante,
    EventoParticipante,
    Equipo
)

# ─────────────────────────────────────────────
# INLINE PARA LA RELACIÓN MANY-TO-MANY (THROUGH)
# ─────────────────────────────────────────────
class EventoParticipanteInline(admin.TabularInline):
    model = EventoParticipante
    extra = 1


# ─────────────────────────────────────────────
# DEPORTE
# ─────────────────────────────────────────────
@admin.register(Deporte)
class DeporteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_creacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)


# ─────────────────────────────────────────────
# PARTICIPANTE
# ─────────────────────────────────────────────
@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'apellido',
        'email',
        'telefono',
        'fecha_creacion'
    )
    list_filter = ('fecha_creacion',)
    search_fields = ('nombre', 'apellido', 'email')
    ordering = ('apellido', 'nombre')


# ─────────────────────────────────────────────
# EVENTO
# ─────────────────────────────────────────────
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'deporte',
        'fecha',
        'lugar',
        'fecha_creacion'
    )
    list_filter = ('deporte', 'fecha', 'fecha_creacion')
    search_fields = ('nombre', 'lugar', 'descripcion')
    ordering = ('-fecha',)
    date_hierarchy = 'fecha'
    inlines = [EventoParticipanteInline]  # 👈 CLAVE


# ─────────────────────────────────────────────
# EVENTO PARTICIPANTE (MODELO INTERMEDIO)
# ─────────────────────────────────────────────
@admin.register(EventoParticipante)
class EventoParticipanteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'evento',
        'participante',
        'fecha_inscripcion',
        'numero_inscripcion'
    )
    list_filter = ('fecha_inscripcion', 'evento')
    search_fields = (
        'evento__nombre',
        'participante__nombre',
        'participante__apellido',
        'numero_inscripcion'
    )
    ordering = ('-fecha_inscripcion',)


# ─────────────────────────────────────────────
# EQUIPO
# ─────────────────────────────────────────────
@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'deporte', 'fecha_creacion')
    list_filter = ('deporte', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)
